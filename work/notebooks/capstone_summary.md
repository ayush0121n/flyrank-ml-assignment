# Capstone Summary — CTR / Engagement Opportunity Scoring

**Lane:** CTR / Engagement Opportunity Scoring  
**Author:** Ayush Narkhede  
**Metrics receipt:** `work/outputs/capstone_metrics.json`

## Key results (client-holdout test set)

| Model              | ROC-AUC | Average Precision |
|--------------------|---------|-------------------|
| Rule baseline      | 0.577   | 0.305             |
| Logistic Regression| 0.769   | 0.524             |
| Random Forest      | 0.779   | 0.531             |
| **Gradient Boosting** | **0.781** | **0.547**     |

- Test N = 9 356 content items  
- Positive rate ≈ 22.6 %  
- Top features: `ctr_may`, `impr_may`, `clicks_may`, `avg_pos_may`

## How to reproduce

1. Accept HF gate for `FlyRank/internship-warehouse` and set `HF_TOKEN`.
2. Aggregate May (features) + June (label) via DuckDB over `hf://`.
3. Join `dim_content` static attributes.
4. Define binary opportunity label on June CTR.
5. Client-level 70/30 holdout, seed 42.
6. Train LR / RF / GB; evaluate on same split.

Full narrative lives in the deployed paper:  
https://ayush0121n.github.io/flyrank-ml-assignment/submission/
