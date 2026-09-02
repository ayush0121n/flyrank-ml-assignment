# Tell the Story — demo outline + shareable cuts

**Paper:** https://ayush0121n.github.io/flyrank-ml-assignment/submission/

## 5-minute demo outline

1. **Question (45s)** — Among pages that already get impressions, which under-capture clicks—and can we rank them better than a rule?
2. **Method (60s)** — May features → June label; client-holdout; no June metrics in X.
3. **One chart (75s)** — AUC bars: baseline 0.577 vs GB 0.781 (base rate ~22.6%).
4. **Honest result (60s)** — Lift on held-out clients; observational, not causal.
5. **One recommendation (60s)** — Tier-1: title/meta review for low prior CTR + solid impressions; never auto-publish.

## Social post

Just shipped my FlyRank ML capstone: ranking CTR opportunity on real search performance data.

Method: prior-month GSC + content features → next-month under-capture label → client-holdout → GB AUC 0.781 vs rule baseline 0.577.

A review queue for editors—not a promise that rewrites will grow traffic.

## Employer summary (3 sentences)

I built a CTR / engagement opportunity model on the FlyRank internship warehouse (monthly GSC aggregates + content attributes; May features → June labels). On a client-level holdout, gradient boosting ranked under-capturing pages at ROC-AUC 0.781 versus a 0.577 rule baseline (base rate ≈ 22.6%). The deliverable is a decision-support action playbook—ranked review tiers with reason codes—not automated publishing or causal traffic claims.
