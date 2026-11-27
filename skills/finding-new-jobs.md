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

## Before adding — the verify gates (27 Nov 2026 audit of all 74 rejected jobs)

The audit found 12 jobs that were rejected but could have been applied to. Most of the waste came from adding jobs before checking them properly. These gates apply BEFORE any job is added to the dashboard:

1. **Read the full description first.** Never add a job from a title or an aggregator snippet alone. If the full description shows no WordPress, PHP or CMS work, do NOT add it — log it as rejected in seen-jobs.md with the reason. This alone would have prevented 29 "not a WordPress role" rejections (React, Python, .NET, Drupal-adjacent and Magento roles added from titles, then rejected after someone finally read the description).
2. **Verify the apply route before adding.** Confirm there is a working apply route — an employer form that loads, an email address, or a live board link. A dead route (404, no form, no role on the employer board) means the job is held or rejected, never New. This would have prevented the Sumeru, Planet Pharma and Moxie360 cases, which had no apply route from day one.
3. **Aggregator dates are not dates.** Never add a job on a Jooble, phpjobs.io or CodeMind date alone. Confirm the posted date on the original posting or the employer site. If the date cannot be confirmed, the job stays HELD (like Awesome Motive Junior and MERAK), never added.
4. **Judge the stack, not the title.** PHP, Laravel, Drupal and enterprise-CMS roles are IN scope when the core work is PHP/CMS — Javed already applied to a Senior Drupal Developer role and to PHP-heavy backend roles. Do not reject a role just because WordPress is not named; read the full description and judge the actual work.
5. **Re-verify before rejecting as closed.** A "closed" rejection needs TWO checks (the aggregator/board AND the employer's own careers page). A Built In or Indeed "removed/expired" notice must be confirmed in the live browser — text fetch serves stale cache (SpecterOps, AON #17, Limble #142 and Gemini #181 all looked closed in text fetch and were live).
6. **Occasional travel is HELD, not rejected.** A role that requires occasional offsite travel is held for Javed's decision (like #64 Aretum), never auto-rejected and never auto-added.
7. **Correct the employer name.** When an aggregator mislabels the employer (Takeda was really Focus Financial Partners; "Remote Services Inc." was really Wing Assistant), record the real employer name with a note. Never apply under the wrong company name.
8. **Speed matters more than discovery.** Most "closed" rejections were jobs that were live when added and closed before anyone applied. A job added today should be applied to within 24 hours. Prioritise by score and closing risk (contract and short-window roles first).
9. **Log every rejection at rejection time.** Every rejection gets a dated reason in seen-jobs.md the moment it is rejected, so a later sweep never re-adds it and the next audit never re-checks it blind.

## Restores from the 27 Nov 2026 audit

12 jobs were restored to New after live re-verification: #112 Zortech, #80 MD Integrations, #97 Ad Hoc, #83 Focus Financial Partners (listed as Takeda — restore only after remote is confirmed), #129 Calendly (only if Javed accepts occasional offsite travel), #17 AON, #142 Limble, #106 Talent Groups, #104 Zephyrline, #101 Wing Assistant (listed as Remote Services Inc.), #143 Crowd Favorite, #181 Gemini. Confirmed closed and left rejected: Sumeru, Planet Pharma, Moxie360, Mondo, Rankings.io, BD&J, Patrick Industries, Saxon #111, Melon Local (live but on-site), PhotoShelter, Coinbase, Aquent #1.
