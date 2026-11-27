#!/usr/bin/env python3
"""Backup after every round for Javed's job search.
Usage: python3 backup_round.py [round-name]
Creates ~/workspace/javed-job-search/backups/<YYYY-MM-DD-HHMM>-<round-name>/
with copies of: seen-jobs.md, best-100.md, portfolio HTML, master CV,
SpecterOps CV, deploy scripts, and a manifest with counts.
"""
import shutil, sys
from datetime import datetime
from pathlib import Path

H = Path.home()
SRC = H / "workspace"
BACKUPS = SRC / "javed-job-search" / "backups"

FILES = [
    ("javed-job-search/seen-jobs.md", "seen-jobs.md"),
    ("javed-portfolio/best-100.md", "best-100.md"),
    ("your_files/javed-iqbal-portfolio/javed-iqbal-portfolio.html", "portfolio.html"),
    ("your_files/javed-iqbal-job-dashboard/javed-iqbal-job-dashboard.html", "dashboard.html"),
    ("your_files/javed-iqbal-master-cv/javed-iqbal-master-cv.docx", "master-cv.docx"),
    ("your_files/javed-iqbal-cv-specterops/javed-iqbal-cv-specterops.docx", "specterops-cv.docx"),
    ("javed-job-search/deploy_portfolio_vercel.py", "deploy_portfolio_vercel.py"),
]

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "round"
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    dest = BACKUPS / f"{stamp}-{name}"
    dest.mkdir(parents=True, exist_ok=False)
    lines = [f"Backup {stamp} - {name}", ""]
    for rel, out in FILES:
        src = SRC / rel
        if src.exists():
            shutil.copy2(src, dest / out)
            lines.append(f"OK {out} ({src.stat().st_size} bytes)")
        else:
            lines.append(f"MISSING {rel}")
    (dest / "MANIFEST.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("Backup folder:", dest)

if __name__ == "__main__":
    main()
