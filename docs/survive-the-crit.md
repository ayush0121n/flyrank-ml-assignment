# Survive the Crit — Design review package

**Portfolio reviewed:** https://ayush0121n.github.io/flyrank-ml-assignment/  
**Also considered:** https://ayushdevxx.vercel.app/  
**Date:** 29 Aug 2026

---

## 1. Proof statement (what this page is hired to prove)

> **I build applied machine learning on real search data — and ship the full-stack systems around it.**

Evidence on the page: FlyRank CTR opportunity model (client-holdout AUC 0.781), public research paper, DevTriage AI agent with live tool + run capture, working contact form.

---

## 2. Reviewer feedback (second pair of eyes)

**Q1 — In ten seconds, what do you do?**  
*Before fixes:* “AI/ML and full-stack… intern… MCA…” — too many labels; the one job was fuzzy.  
*After:* One sentence at the top states the job; the next block shows a measured result.

**Q2 — Would you believe you’re good at it?**  
*Before:* FlyRank numbers were buried under Experience; projects had no proof links; “Main portfolio site” competed with this page.  
*After:* Proof block leads with AUC + agent; paper / agent / repo are one click from the top; single primary CTA (“Contact / Hire me”).

### Other feedback collected

| Feedback | Sort |
|----------|------|
| Opening tagline listed too many roles → unclear in 10 seconds | **Must-fix** |
| Strongest proof (AUC, paper, agent) sat too low on the page | **Must-fix** |
| “Main portfolio site” button created two competing homes | **Must-fix** |
| Projects described but no live demo / repo links for each | **Must-fix** (partial: profile link added; per-repo URLs still nice-to-have) |
| About paragraph started with “Versatile” (weak) | **Must-fix** |
| Phone number on public page (privacy) | **Must-fix** (already removed) |
| Vercel site is visually strong but scroll height / nav on mobile needs owner check | **Nice-to-have** (Vercel source not in this repo) |
| Add FlyRank completion badge later | **Nice-to-have** (blocked on capstone approval) |
| More project screenshots | **Nice-to-have** |

---

## 3. Must-fix vs nice-to-have

### Must-fix (done on the live GitHub Pages site)
1. Sharp **proof statement** in the header (one job, one sentence).
2. **Proof section** moved to the top with the AUC number and agent in plain view.
3. Removed dual-portfolio confusion; this page is self-contained; primary CTA is Contact.
4. Experience cards link straight to paper, agent, audit notebook.
5. Phone number removed from public HTML.
6. Mobile: 44px+ tap targets, readable type, no horizontal overflow on the pages we control.

### Nice-to-have (later)
- Per-project GitHub repo URLs and live demos when public.
- FlyRank badge after capstone approval.
- Vercel-only animation / scroll polish (owner’s other host).

---

## 4. Evidence of fixes on the live site

| Fix | Live evidence |
|-----|----------------|
| Proof statement in header | https://ayush0121n.github.io/flyrank-ml-assignment/ |
| Proof block with AUC 0.781 + agent | same URL, section “What I do (and the proof)” |
| Contact form working | https://ayush0121n.github.io/flyrank-ml-assignment/contact.html |
| Paper / agent / audit linked | buttons under Experience + Proof |
| No phone number | view-source: no `tel:` or `7972853182` |
| Crit + sort documented | this file: `docs/survive-the-crit.md` |

---

## 5. Engagement note (no defending)

I treated the 10-second confusion as a real failure, not a “reader didn’t scroll” problem. The page now leads with the job and the measured work. Remaining gaps (per-project links, Vercel polish) are logged as nice-to-have, not excuses.

---

*Reviewer role: critical second pair of eyes (design + clarity).  
Member: Ayush Narkhede · github.com/ayush0121n*
