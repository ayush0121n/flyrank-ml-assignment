# Break Your Own Site — Diligence log

**Sites tested:**  
- https://ayush0121n.github.io/flyrank-ml-assignment/  
- https://ayush0121n.github.io/flyrank-ml-assignment/contact.html  
- https://ayush0121n.github.io/flyrank-ml-assignment/submission/  
- https://ayushdevxx.vercel.app/ (owner brand site; noted only)

**Date:** 2 Sep 2026

---

## 1. How I tried to break it

| Attack | Result | Notes |
|--------|--------|-------|
| Empty form submit | Browser `required` blocks; JS backup also blocks | Fixed/hardened |
| Garbage email (`not-an-email`) | HTML5 `type=email` + JS regex reject | Fixed/hardened |
| Very short message | JS rejects length &lt; 3 | Fixed |
| Double-click Send fast | Button disables during request; stays disabled 2.5s after success | Fixed |
| Missing / wrong access key | Clear error message; no silent fail | OK |
| **Critical bug found** | JS compared access key to the *real* key and treated a valid key as “not activated” — form could never succeed | **Fixed** |
| “Back to portfolio” on contact | Pointed at Vercel only; broken mental model for GitHub Pages visitors | **Fixed** → `./` |
| All major links (paper, repo, agent video, contact) | HTTP 200 | OK |
| Mobile viewport contact form | Readable; 16px inputs; 48px button | OK |
| Pages without Open Graph tags | Weak social-share preview | **Fixed** — og/twitter meta added |
| No robots.txt / sitemap | Harder for crawlers | **Fixed** |

---

## 2. Findability & speed

### SEO / meta added
- Unique `<title>` + `<meta name="description">` on index and contact  
- `canonical`, `og:title`, `og:description`, `og:url`, `twitter:card`  
- `robots.txt` + `sitemap.xml` at site root  

### Findability
- Portfolio is public at a stable GitHub Pages URL  
- Linked from repo README context and LinkedIn (owner action)  
- Name + “FlyRank” + project terms appear in page text for search  

### Speed (honest, free-tier check)
- Index HTML ~10 KB, contact ~5 KB — static, no heavy JS frameworks on GitHub Pages pages  
- GitHub Pages CDN + HTTPS; no oversized images on these pages  
- **Known limitation:** Full Lighthouse/PageSpeed score depends on network; Vercel brand site is a separate deploy with its own assets  

---

## 3. Triage

### Fix-now (done on live GitHub Pages)
1. Form activation bug that blocked successful submits  
2. Client-side empty / invalid-email / short-message guards  
3. Double-submit lock after success  
4. Contact “Back to portfolio” → local `./`  
5. Full SEO meta + Open Graph + Twitter cards  
6. `robots.txt` + `sitemap.xml`  

### Known limitations (named, not hidden)
| Limitation | Why it remains |
|------------|----------------|
| Web3Forms access key is in page source | Client-side form services work this way on free tier; key only authorises this form endpoint, not account takeover |
| Form API rejects non-browser server POSTs | Free plan is client-side only — by design |
| Project cards lack per-repo live demos | Nice-to-have; GitHub profile linked |
| Vercel site scroll/animation behaviour | Different host; not this repo’s static pages |
| Cold GitHub Pages cache (~minutes after push) | Host behaviour; hard-refresh clears |
| Social image (`og:image`) not set | Optional asset; text OG tags are present |

---

## 4. Hardening review (structured self + second-pass checklist)

Reviewed against: empty input, garbage input, double submit, link integrity, mobile, SEO, honesty about limits.

**Must-fixes from review → all addressed on live site** (see section 3).  
**Known limitations → documented above**, not papered over.

Evidence:
- Fixed form + SEO: https://ayush0121n.github.io/flyrank-ml-assignment/contact.html  
- Portfolio with meta: https://ayush0121n.github.io/flyrank-ml-assignment/  
- This log: `docs/break-your-own-site.md`  
- robots/sitemap: `/robots.txt`, `/sitemap.xml`

---

*Ayush Narkhede · General AI Fluency · Break Your Own Site · Diligence checkpoint*
