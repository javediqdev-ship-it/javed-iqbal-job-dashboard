#!/usr/bin/env python3
"""Deploy Javed Iqbal's portfolio and job dashboard to Vercel using HIS OWN
account token (passed via VERCEL_TOKEN env var, never stored in this file).
Direct Vercel REST API calls, no teamId, no MCP wrapper, no other account.
"""
import hashlib, json, os, sys, time, urllib.request, urllib.error
from pathlib import Path

TOKEN = os.environ.get("VERCEL_TOKEN")
if not TOKEN:
    print("VERCEL_TOKEN env var is missing"); sys.exit(1)

BASE = "https://api.vercel.com"
HOME = Path.home()
SITES = [
    ("javed-iqbal-portfolio",
     HOME / "workspace/your_files/javed-iqbal-portfolio/javed-iqbal-portfolio.html"),
    ("javed-iqbal-job-dashboard",
     HOME / "workspace/your_files/javed-iqbal-job-dashboard/javed-iqbal-job-dashboard.html"),
]
# Extra real files served alongside the page, keyed by project name.
# (archive path in the deployment, source file on disk)
EXTRA_FILES = {
    "javed-iqbal-job-dashboard": [
        ("assets/javed-iqbal-cv-specterops.docx",
         HOME / "workspace/your_files/javed-iqbal-cv-specterops/javed-iqbal-cv-specterops.docx"),
        ("assets/javed-iqbal-cv-specterops.pdf",
         HOME / "workspace/your_files/javed-iqbal-cv-specterops/javed-iqbal-cv-specterops.pdf"),
    ],
}
# Every other CV lives in the goal files folder, one folder per CV:
# javed-iqbal-cv-<slug>/javed-iqbal-cv-<slug>.docx/.pdf (plus the master CV).
# Glob them so new CVs are deployed automatically; never hardcode the list.
_GOAL_FILES = HOME / "workspace/goals/javed-iqbal-remote-wordpress-job-search/files"
for _cv in sorted(_GOAL_FILES.glob("javed-iqbal-cv-*")) + sorted(_GOAL_FILES.glob("javed-iqbal-master-cv")):
    for _src in sorted(_cv.glob("javed-iqbal-*.docx")) + sorted(_cv.glob("javed-iqbal-*.pdf")):
        EXTRA_FILES["javed-iqbal-job-dashboard"].append((f"assets/{_src.name}", _src))

# Deploy one site only when SITE is set, e.g. SITE=javed-iqbal-job-dashboard
_only = os.environ.get("SITE")
if _only:
    SITES = [s for s in SITES if s[0] == _only]
    if not SITES:
        print("Unknown SITE:", _only); sys.exit(1)

def call(method, path, body=None, raw=None, extra_headers=None):
    url = BASE + path
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    if raw is not None:
        req.add_header("Content-Type", "application/octet-stream")
    elif body is not None:
        req.add_header("Content-Type", "application/json")
    for k, v in (extra_headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        try:
            detail = json.loads(e.read() or b"{}")
        except Exception:
            detail = {}
        return e.code, detail

# 0. Verify the token belongs to Javed's account
status, me = call("GET", "/v2/user")
print("token check:", status, "username:", me.get("user", {}).get("username"))
if status != 200:
    print("TOKEN INVALID:", json.dumps(me)[:500]); sys.exit(1)

for project, html_path in SITES:
    raw = html_path.read_bytes()
    sha1 = hashlib.sha1(raw).hexdigest()
    print(f"\n== {project} ({len(raw)} bytes, sha1 {sha1[:12]}...) ==")

    # 1. Create project (409 = already exists, fine)
    status, res = call("POST", "/v9/projects", {"name": project})
    print("create_project:", status, res.get("name") or res.get("error", {}).get("message"))

    # 2. Create production deployment (inline base64 file data; this
    # account's API rejects the sha-based files format)
    import base64 as _b64
    files = [{"file": "index.html",
              "data": _b64.b64encode(raw).decode(),
              "encoding": "base64"}]
    # Extra real files served alongside the page (so download links open
    # as proper files with a filename, instead of an embedded data link).
    for arc, src in EXTRA_FILES.get(project, []):
        data = Path(src).read_bytes()
        files.append({"file": arc,
                      "data": _b64.b64encode(data).decode(),
                      "encoding": "base64"})
        print("extra file:", arc, len(data), "bytes")
    status, res = call("POST", "/v13/deployments", {
        "name": project,
        "files": files,
        "target": "production",
        "projectSettings": {"framework": None},
    })
    if status not in (200, 201):
        print("DEPLOY FAILED:", status, json.dumps(res)[:800]); sys.exit(1)
    dep_id = res.get("id")
    print("deployment id:", dep_id, "| url:", res.get("url"), "| state:", res.get("readyState"))

    # 4. Poll until READY
    for _ in range(24):
        time.sleep(5)
        status, res = call("GET", f"/v13/deployments/{dep_id}")
        state = res.get("readyState")
        if state == "READY":
            print("READY:", res.get("url"))
            break
        if state == "ERROR":
            print("BUILD ERROR:", json.dumps(res)[:800]); sys.exit(1)
    else:
        print("TIMED OUT waiting for READY"); sys.exit(1)

    # 5. Verify the production alias serves the page
    alias = f"https://{project}.vercel.app/"
    try:
        with urllib.request.urlopen(alias, timeout=30) as r:
            print("live check:", alias, "->", r.status)
    except urllib.error.HTTPError as e:
        print("live check:", alias, "-> HTTP", e.code)
    except Exception as e:
        print("live check failed:", e)
