# Retrospective — for the person I was in Week 1

**Ayush Narkhede · FlyRank ML + AI Fluency · ~800 words**

Week 1 me thought the internship would be mostly notebooks: load data, fit a model, paste a score. I was wrong about where the work actually lives. The score was the easy middle. The hard parts were the edges—honest splits, claim language, a paper someone else can read, and an agent that is useful without being dangerous.

## What I set out to do

I joined to learn applied search intelligence and to ship something public with my name on it. The ML track promised real warehouse data; the fluency track promised a personal agent and a live site. My private goal was simpler: stop being only a student who *trains* models and become someone who can *defend* them.

## What changed

Three shifts matter more than any single AUC number.

**1. Validation before vibes.**  
A random split made the CTR opportunity model look stronger than it was. A client-holdout dropped the fantasy and left Gradient Boosting at **0.781 ROC-AUC** against a **0.577** rule baseline, with a **22.6%** base rate on the table. That gap between “looks good” and “holds on unseen clients” changed how I read every metric I see online. I now reach for the split design before I reach for the leaderboard screenshot.

**2. Language is part of the model.**  
“Will increase traffic” is a different product than “ranks pages for review.” Writing the paper and the action playbook forced me to stay on the second sentence. Decision-support, observed association, no auto-publish. That is not soft skills padding—it is how you keep a portfolio from lying.

**3. Ship loops, not slides.**  
The agent (DevTriage AI) only became real when it ran end-to-end: ingest → classify → draft → `triage_digest.md`, with **no send**. Breaking my own contact form found a bug that would have blocked every successful submit. Mobile, SEO, badge, analytics—the boring checklist is what makes a site feel trustworthy instead of temporary.

AI pair-programming accelerated scaffolding and prose. What I had to own myself: the leakage checklist, the client-holdout number, the safety boundary on the agent, and the diligence logs when something failed.

## What I’d build next

- A monthly refresh job that rebuilds the opportunity queue when a new GSC month lands, with monitoring triggers already listed in the playbook.  
- Richer agent tools (calendar, email) still behind explicit human approval.  
- Per-project live demos linked from the portfolio, and an official FlyRank credential ID on the badge when issued.

## Three transferable things

1. **Attack your own split.** If the honest split collapses the score, that collapse *is* the finding.  
2. **Propose, don’t act.** Drafts and ranked queues beat silent automation in a portfolio and in production trust.  
3. **Write the limitation before the highlight.** Reviewers and employers hear confidence in what you refuse to claim.

## To Week 1 me

Clone the repo. Run the agent once offline. Open the paper. Read the validation notebook. The point was never a perfect model—it was a public, inspectable system you can explain without flinching. You have that now:

- Paper: https://ayush0121n.github.io/flyrank-ml-assignment/submission/  
- Portfolio: https://ayush0121n.github.io/flyrank-ml-assignment/  
- Repo: https://github.com/ayush0121n/flyrank-ml-assignment  

Hours belong in the portal log. The work belongs in the links.
