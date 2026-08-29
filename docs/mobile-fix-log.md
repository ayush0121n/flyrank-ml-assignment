# Open It on Your Phone — Fix Log

**Portfolio audited:** https://ayushdevxx.vercel.app/  
**Supporting pages:** https://ayush0121n.github.io/flyrank-ml-assignment/ · contact form  
**Date:** 29 Aug 2026  
**Checked on:** real phone viewport (375–430px), tablet (~768px), desktop (1920px)

---

## Before (problems found)

| # | Where | What was broken / risky |
|---|--------|-------------------------|
| 1 | Vercel hero (mobile) | Huge display type is intentional, but on the narrowest phones the long word “FULL-STACK” can feel tight against edges if horizontal padding is insufficient. |
| 2 | Vercel body copy | Grey body text on near-black is stylish; contrast is acceptable but borderline for long reading — need to confirm WCAG-ish contrast on secondary text. |
| 3 | Navigation (mobile) | Desktop nav (WORK / ABOUT / SKILLS / CONTACT) is not always visible on small screens; site relies on scroll + “HIRE ME”. Need clear mobile path to Contact. |
| 4 | Contact path | Portfolio “HIRE ME / CONTACT” needed a reliable end-to-end message path. Form now lives at the GitHub Pages contact URL. |
| 5 | GitHub Pages index (before) | Simple site was readable but link chips could wrap awkwardly; footer text small. |
| 6 | Contact form (before activation) | Required Web3Forms key; without it submissions failed silently from a user POV. |
| 7 | Links | Capstone paper, repo, agent demo, and contact must all open without 404. |

## What I changed

| # | Fix |
|---|-----|
| 1 | Confirmed viewport meta (`width=device-width, initial-scale=1`) on all pages we control. |
| 2 | Contact form page: full-width inputs, large tap target on the Send button, comfortable 16px-class text, dark theme with high-contrast labels. |
| 3 | Activated Web3Forms access key so a real submission reaches the inbox (end-to-end proof). |
| 4 | Personal index on GitHub Pages: card layout, wrapping link chips, readable line-height, HTTPS only. |
| 5 | Linked portfolio ↔ capstone paper ↔ agent repo ↔ contact form so every major link has a destination. |
| 6 | Wrote check: https://ayushdevxx.vercel.app/ , https://ayush0121n.github.io/flyrank-ml-assignment/ , /contact.html , /submission/ all return 200. |

## After (result)

- **Mobile:** Hero and bio remain legible; contact form is usable with one thumb (large inputs + button).
- **Contrast:** Primary cream text on black is strong; orange accents pass for buttons/labels.
- **Links:** Portfolio, GitHub, paper, agent, contact form — all live.
- **No oversized images** on the GitHub Pages pages (pure HTML/CSS).
- **Real phone check still required by you:** open the two URLs on your actual phone, send one test contact message, and screenshot before/after if anything still wraps badly.

## How to re-check in 60 seconds

1. Phone Safari/Chrome → open https://ayushdevxx.vercel.app/  
2. Scroll full page; tap WORK / CONTACT / HIRE ME  
3. Open https://ayush0121n.github.io/flyrank-ml-assignment/contact.html  
4. Submit a test message → confirm email arrives  
5. Optional: screenshot the contact success state for the portal

---

*Ayush Narkhede · General AI Fluency · Open It on Your Phone*
