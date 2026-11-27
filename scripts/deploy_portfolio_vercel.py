#!/usr/bin/env python3
"""Deploy Javed Iqbal's portfolio (single exported HTML) to Vercel.
Follows the proven pattern in client-review-dashboard/deploy_vercel.py:
upload_file (base64) then create_deployment. No teamId anywhere.
"""
import base64, hashlib, json, subprocess, sys
from pathlib import Path

V = "/opt/hatch/bin/vercel"
HTML = Path.home() / "workspace/your_files/javed-iqbal-portfolio/javed-iqbal-portfolio.html"
PROJECT = "javed-iqbal-portfolio"

def call(tool, args):
    r = subprocess.run([V, "call-tool", "--name", tool, "--arguments-json",
                        json.dumps(args)], capture_output=True, text=True)
    try:
        out = json.loads(r.stdout)
    except json.JSONDecodeError:
        print("RAW:", r.stdout, r.stderr); sys.exit(1)
    if not out.get("ok", True):
        print("FAILED", tool, json.dumps(out, indent=2)[:3000]); sys.exit(1)
    return out

# 1. Create the project (ignore if it already exists)
res = call("create_project", {"requestBody": {"name": PROJECT}})
print("create_project:", json.dumps(res)[:800])

# 2. Upload index.html
raw = HTML.read_bytes()
sha1 = hashlib.sha1(raw).hexdigest()
res = call("upload_file", {
    "requestBody": base64.b64encode(raw).decode(),
    "xVercelDigest": sha1,
    "contentLength": len(raw),
})
print("uploaded index.html", len(raw), "bytes, sha1", sha1, "->", json.dumps(res)[:300])

# 3. Create production deployment
res = call("create_deployment", {
    "requestBody": {
        "name": PROJECT,
        "project": PROJECT,
        "target": "production",
        "files": [{"file": "index.html", "sha": sha1, "size": len(raw)}],
    }
})
print(json.dumps(res, indent=2)[:3000])
