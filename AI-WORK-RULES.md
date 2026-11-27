# AI Work Rules — one AI at a time

Two AIs share this repo (job-search AI and interview-trainer AI).
Both edit the same files, especially the 3+ MB `index.html`.
On 27 Nov 2026 the interview-training section was overwritten because
one AI pushed `index.html` from a stale local copy. These rules stop that.

## Rule 1 — LOCK (must follow, no exceptions)

Before editing `index.html` or deploying to Vercel:

1. Check `.ai-lock.json` on `main` (GitHub API or a fresh pull).
2. If it exists and is less than 2 hours old: **STOP. Do not edit, do not
   push, do not deploy.** Wait. Do your reading / prep work that does not
   touch `index.html` instead.
3. If it does not exist, or is older than 2 hours: create it first and
   push it (own commit) before you touch anything else:
   `{"holder": "<your name>", "task": "<what you will do>",
   "started_utc": "<ISO time>", "expires_utc": "<started + 2h>"}`
4. Delete the lock (own commit) as soon as your work is pushed AND
   deployed AND verified live. Never leave a lock behind.
5. Only the lock holder deploys. Never deploy while someone else holds
   the lock.
6. A stale lock (> 2h) may be removed, but only after checking the
   Vercel deployments list — the holder may be mid-deploy.

## Rule 2 — FRESH COPY (the rule that prevents overwrites)

- Always pull the latest `main` immediately before editing `index.html`.
- Never push `index.html` from a copy older than the latest commit on
  `main`. Check `git log -1` / the GitHub commits API first.
- If `main` moved while you were working, **re-apply your changes onto
  the new file**. Never push your old copy over the new one.
- A failed push (409 / sha mismatch) means someone else moved first:
  pull fresh, re-apply, try again. Do not force-push. Ever.

## Rule 3 — PROTECTED SECTIONS (never delete)

`index.html` contains a marked Interview Training section. Do not remove it:
- sidebar button `data-nav="training"` (after Interviews, before CVs)
- mobile bottom-nav button `data-nav="training"`
- `training: [...]` entry inside `TITLES`
- `<section class="view" id="view-training">` with the full prep
- "Practise now — Interview Training" button in the Interviews empty state

If your local copy of `index.html` does NOT contain `view-training`,
your copy is stale — pull fresh (Rule 2). Do not "fix" it by pushing.

Same protection applies to `training.html`, `skills/interview-trainer.md`
and everything under `interview-prep/`. Update them, never delete them.

## Rule 4 — DEPLOY

- Vercel is NOT Git-linked. A GitHub push alone does NOT deploy.
- After pushing, the lock holder deploys manually
  (`vercel deploy --prod`) and verifies the live URLs.
- Verify live after every deploy: the new content must be present AND
  the other AI's latest changes must still be present. If either is
  missing, say so — do not silently re-deploy over it.

## Rule 5 — SMALL STEPS

- One logical change per commit, with a commit message that says what
  changed and why.
- Never rewrite `index.html` wholesale from memory. Edit the file you
  pulled.

Owner: Mubashir. He can break a lock. No AI may break another AI's lock
except the stale-lock case in Rule 1.6.
