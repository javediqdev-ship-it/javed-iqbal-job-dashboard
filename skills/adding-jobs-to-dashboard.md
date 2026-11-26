# Adding Jobs to the Dashboard

How a new job gets onto the job dashboard. This file is the living record — update it whenever the dashboard or the deploy changes.

## The dashboard

- Name: Javed Iqbal Job Dashboard. Live at https://javed-iqbal-job-dashboard.vercel.app/
- Style: Upastra purple. Deep-purple sidebar on desktop, bottom navigation on mobile. Fully responsive.
- Pages: Overview, New Jobs, Applied Jobs, Responses, Interviews, CVs, Rejected. One job detail page per job (title, company, category, pills, status, match score with reasons, full description, responsibilities, required skills, about the company, pay, posted/found dates, source platform, Apply / View original posting / company website buttons, "Which CV to use" panel, timeline, notes, interview prep points, 3 similar jobs).
- Password lock: page-side lock, SHA-256 hash in code, casual deterrent only (not server-grade security). Unlock lasts for the browser session.
- Filters on New Jobs: Source filter (every source with job count), Status filter (All / Not applied / Applied, default Not applied), Sort filter (Latest first default, Oldest first, Highest score, Lowest score). Choice saved in browser localStorage.
- Applied/Rejected tracking: every job row and detail page has "Mark Applied" and "Reject" actions. Reject needs a reason. Rejected jobs move to the Rejected page with the reason, date and a Restore button. All state saves in the browser (localStorage key ji_job_state).

## The update flow (every time jobs are added)

1. Edit the dashboard artifact with the new jobs (title, company, score, pay, dates, source, link, description, requirements).
2. Export the artifact to a single HTML file.
3. Grep-verify the export: new job names and features must be in the file (claims about the export have been wrong before — always re-export and verify).
4. Deploy to Vercel (Javed's own account javediqdev-7573): script ~/workspace/javed-job-search/deploy_javed_vercel.py, direct Vercel REST API, token from the VERCEL_TOKEN env var (never stored in any file; Javed pastes it in chat, used transiently once). Verify the live site after deploy (byte-identical check).
5. Run a backup (backup_round.py).
6. Push the updated files to GitHub (see the repo README): index.html, cv-master.md, cv-instructions.md, skills/, sources.md, seen-jobs.md. GitHub push needs Javed's GitHub token pasted in chat, used transiently once (never stored).
7. Report the new jobs in the chat.

## The CVs page

- Every tailored CV gets its link on the dashboard CVs page (Open + Download, PDF format).
- Every job detail page has a "CV link for this job" section: the tailored CV if one exists, otherwise "No tailored CV yet for this job" with a "Go to CVs page" button.

## What never happens

- Never add a job twice (dedupe by company + title + source link; check seen-jobs.md first).
- Never add a job with no individual link, an onsite/hybrid role, or a location outside USA/Canada/UK.

## Note — two different dashboards

This dashboard is Javed's job dashboard. It is NOT Marshal's Upastra team dashboard (dashboard.jehanzaib007.com), which has a permanent read-only rule: never make any change inside it. Do not confuse the two.
