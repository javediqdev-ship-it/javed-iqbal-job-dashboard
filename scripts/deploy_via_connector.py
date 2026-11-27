#!/usr/bin/env python3
"""Deploy Javed Iqbal's job dashboard to Vercel through the connected
Vercel MCP connector (OAuth, Javed's account javediqdev-7573).
No API token is used or stored here. Flow: upload each file with the
connector's upload_file tool (returns a SHA1 digest), then create the
deployment referencing the files by SHA1 and size, poll until READY,
and live-check the production alias.
Usage: python3 deploy_via_connector.py [--site javed-iqbal-job-dashboard]
"""
import base64
import hashlib
import json
import subprocess
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

VERCEL = "/opt/hatch/bin/vercel"
HOME = Path.home()

DASHBOARD_HTML = HOME / "workspace/your_files/javed-iqbal-job-dashboard/javed-iqbal-job-dashboard.html"
EXTRA_FILES = [
    ("assets/javed-iqbal-cv-specterops.docx",
     HOME / "workspace/your_files/javed-iqbal-cv-specterops/javed-iqbal-cv-specterops.docx"),
    ("assets/javed-iqbal-cv-specterops.pdf",
     HOME / "workspace/your_files/javed-iqbal-cv-specterops/javed-iqbal-cv-specterops.pdf"),
]
PROJECT = "javed-iqbal-job-dashboard"


def call_tool(name, arguments):
    """Run `vercel call-tool` and return the parsed inner result dict."""
    proc = subprocess.run(
        [VERCEL, "call-tool", "--name", name,
         "--arguments-json", json.dumps(arguments)],
        capture_output=True, text=True, timeout=300,
    )
    if proc.returncode != 0:
        print(f"{name} CLI FAILED rc={proc.returncode}: {proc.stdout[:500]} {proc.stderr[:500]}")
        sys.exit(1)
    try:
        outer = json.loads(proc.stdout)
    except json.JSONDecodeError:
        print(f"{name}: could not parse CLI output: {proc.stdout[:500]}")
        sys.exit(1)
    if not outer.get("ok"):
        print(f"{name}: tool returned not ok: {json.dumps(outer)[:800]}")
        sys.exit(1)
    content = outer.get("result", {}).get("content", [])
    text = "".join(c.get("text", "") for c in content if c.get("type") == "text")
    try:
        inner = json.loads(text)
    except json.JSONDecodeError:
        print(f"{name}: inner text is not JSON: {text[:500]}")
        sys.exit(1)
    return inner.get("result", inner)


def upload_file(arc, path):
    raw = path.read_bytes()
    sha1 = hashlib.sha1(raw).hexdigest()
    print(f"upload {arc}: {len(raw)} bytes, sha1 {sha1[:12]}...")
    res = call_tool("upload_file", {
        "requestBody": base64.b64encode(raw).decode(),
        "xVercelDigest": sha1,
        "contentLength": len(raw),
    })
    print("  upload result:", json.dumps(res)[:300])
    return {"file": arc, "sha": sha1, "size": len(raw)}


def main():
    html = DASHBOARD_HTML.read_bytes()
    html_sha1 = hashlib.sha1(html).hexdigest()
    print(f"dashboard: {len(html)} bytes, sha1 {html_sha1[:12]}...")

    files = [{"file": "index.html", "sha": html_sha1, "size": len(html)}]
    # Upload the HTML itself first so the deployment can reference it.
    res = call_tool("upload_file", {
        "requestBody": base64.b64encode(html).decode(),
        "xVercelDigest": html_sha1,
        "contentLength": len(html),
    })
    print("  upload index.html result:", json.dumps(res)[:300])
    for arc, src in EXTRA_FILES:
        files.append(upload_file(arc, src))

    print("\n== create_deployment ==")
    res = call_tool("create_deployment", {
        "requestBody": {
            "name": PROJECT,
            "files": files,
            "target": "production",
            "projectSettings": {"framework": None},
        }
    })
    print("create_deployment result:", json.dumps(res)[:800])
    dep = res.get("deployment") or res
    dep_id = dep.get("id")
    if not dep_id:
        print("DEPLOY FAILED: no deployment id in result")
        sys.exit(1)
    print("deployment id:", dep_id, "| url:", dep.get("url"), "| state:", dep.get("readyState"))

    for _ in range(24):
        time.sleep(5)
        res = call_tool("get_deployment", {"idOrName": dep_id})
        state = (res.get("deployment") or res).get("readyState")
        print("  state:", state)
        if state == "READY":
            break
        if state == "ERROR":
            print("BUILD ERROR:", json.dumps(res)[:800])
            sys.exit(1)
    else:
        print("TIMED OUT waiting for READY")
        sys.exit(1)

    alias = f"https://{PROJECT}.vercel.app/"
    try:
        with urllib.request.urlopen(alias, timeout=30) as r:
            print("live check:", alias, "->", r.status)
    except urllib.error.HTTPError as e:
        print("live check:", alias, "-> HTTP", e.code)
    except Exception as e:
        print("live check failed:", e)
    print("DONE")


if __name__ == "__main__":
    main()
