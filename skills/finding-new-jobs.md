# Finding New Jobs

How new jobs are found. This file is the living record — update it whenever a source or a method changes.

## Where — the sources

- Master list: sources.md — 50 sources with links.
- Groups: (A) WordPress boards first; (B) LinkedIn public search + Gmail alerts; (C) remote aggregators (Remotive, RemoteOK, We Work Remotely, Himalayas, and others); (D) general boards (Indeed, ZipRecruiter, Jooble, Dice, and others); (E) developer platforms (Wellfound, Arc, Hired, Gun.io, and others); (F) checked, no jobs.
- Never add: Upwork/freelance gig marketplaces, onsite/hybrid roles, jobs outside USA/Canada/UK, jobs with no individual link.

## How — the sweep

1. Twice a day, 05:00 and 17:00 PKT, run a full sweep. Also run extra sweeps when Javed says so — never wait for the next scheduled sweep.
2. Check EVERY source in detail. Check EVERY single listing. Skip NOTHING.
3. Read by text fetch first. For sources text fetch cannot fully check, use the live browser (RemoteOK, RemoteRocketship, RemoteFirstJobs, Dice, WPhired, ZipRecruiter, Rocket.net careers, YC Work at a Startup, Otta, SmartRecruiters, Built In).
4. LinkedIn: Gmail job-alert emails + public search results only. No bots, scripts, scraping or automated Easy Apply (ban risk). VPN must be OFF whenever LinkedIn is opened.
5. Some platforms only open in the USA (for example Recruiter) — a VPN is needed for those. No commercial VPN is installed yet; Tailscale cannot give the browser a US IP.

## Scoring and filters

- WordPress or a related category Javed can do. Remote only (onsite impossible, even day-1 onboarding). USA, Canada, UK.
- Pay over $20/hour is best; pay is otherwise not a filter. Full-time and contract both OK; part-time accepted.
- Junior WordPress and Junior Developer roles preferred and scored HIGHER. Junior window: last 14 days.
- Score 1–10. Pay/date shown as "Not listed" where the source lists none. Never invent jobs, companies, pay or links.

## Dedupe

- A job once added is never added again. Dedupe by company + title + source link.
- Authoritative record: seen-jobs.md. Check it before adding anything.
- Held leads: jobs that fit but are missing a posted date or an individual link stay in seen-jobs.md as held — never added until the date/link is confirmed (examples: Awesome Motive Junior WordPress Developer, MERAK Systems Junior WordPress Developer).

## Caveats

- Aggregator dates (phpjobs.io, Jooble, CodeMind) are re-aggregation dates — cross-check an original before trusting.
- Built In text-fetch crawls are stale cache — only a live-browser check decides live or closed.
- DataDriven Corp listings are aggregator-generated fake employer postings — never add without employer-site verification.
- Watch for spam clusters (junk domains naming real employers) — never add without verification.

## After the sweep

- Add qualifying jobs to the dashboard (see adding-jobs-to-dashboard.md).
- Update seen-jobs.md, run a backup (backup_round.py), report the new jobs in the chat.
- Keep a backup after every round. Backups live in ~/workspace/javed-job-search/backups/.
