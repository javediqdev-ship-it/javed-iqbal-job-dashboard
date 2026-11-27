# Job Search Rules

How jobs are found and scored. This file is the living record — update it whenever a rule changes or a new source is added.

## Hard rule

Never skip a job. Check EVERY source in sources.md (50 sources), check EVERY single listing on each source, and add every qualifying job to the dashboard. If Javed himself finds a new job that was not added, that is failed work. Do not wait for the next scheduled sweep — keep checking with different tries and different approaches.

## Sources

Master source list: ~/workspace/javed-job-search/sources.md — 50 sources with links (WordPress boards first, LinkedIn public search + Gmail alerts, remote aggregators, general boards, developer platforms).

## Scoring

- The job must be WordPress or a related category Javed can do.
- Remote only. Onsite is not possible even for one day (day-1 onsite onboarding also fails).
- Locations: USA, Canada, UK.
- Pay more than $20/hour is best; pay is otherwise not a filter.
- Junior WordPress and Junior Developer roles are preferred and scored HIGHER, not lower. Junior search window: last 14 days.
- Pay/date shown as "Not listed" where the source lists none. Never invent jobs, companies, pay or links.

## Dedupe

A job once added to the dashboard is never added again. Dedupe by company + title + source link. Authoritative record: ~/workspace/javed-job-search/seen-jobs.md.

## Schedule

Twice-daily sweeps at 05:00 and 17:00 PKT. Each run: full sweep of all 50 sources, dedupe, add qualifying jobs, update seen-jobs.md, run a backup, report new jobs. A backup after every round (backup_round.py, backups in ~/workspace/javed-job-search/backups/).

## Caveats

- Aggregator dates (phpjobs.io, Jooble, CodeMind) are re-aggregation dates — always cross-check an original before trusting.
- Built In text-fetch crawls are stale cache — only a live-browser check decides whether a Built In job is live or closed.
- DataDriven Corp listings are aggregator-generated fake employer postings — never add without employer-site verification.
- LinkedIn: no bots, scripts, scraping or automated Easy Apply (ban risk). Read Gmail job-alert emails and public search results only. VPN must be OFF whenever LinkedIn is opened.

## Standing skill rule (set by Javed, 26 Nov 2026)

Javed knows all of WordPress. Any WordPress-related skill can be added to a CV without asking him. WordPress-related includes: hosting, themes, plugins, page builders, analytics, accessibility, design handoffs, performance, security, backups and maintenance. Only a skill clearly outside WordPress work (for example Python, Docker, or CI/CD pipelines) still needs one confirmation from Javed first: collect those into one short list, ask once, and save the answers here. Check this repo before asking Javed anything.

## Self-apply jobs stay in New, never in Rejected (26 Nov 2026)

Jobs Javed will apply to and try himself stay in New Jobs with the Self-apply badge; they are never put in Rejected. This covers every job whose link is a LinkedIn posting (he applies on LinkedIn himself) and any job that cannot be applied to from here but has a route he can try himself. Rejected is only for jobs that are closed and jobs Javed deliberately skips. On the dashboard these jobs carry selfApply: true (or a DEFAULT_SELF_APPLY entry) and are found with the "Self-apply only" filter.

## Work lean and never get stuck on one job (26–27 Nov 2026)

Verify jobs in batches of 3 per browser run, with short briefs and short reports. Closed or non-WordPress jobs get a one-line history entry and a dashboard tag only; the full workflow (tailored CV, QA, submission) is only for jobs that are genuinely WordPress and actually open. Never retry a broken form more than once. If a site blocks a check (a human-verification wall, a sign-in gate), record it as unverifiable and move on — never spend more than a few minutes on one job or one site. Report to the user in one combined report at the end, not per job.
