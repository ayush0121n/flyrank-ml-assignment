# DevTriage AI — Personal Notification Agent

**For:** developers who drown in GitHub notifications and need a ranked daily digest with draft replies—not another inbox.

**What it does:** Pulls GitHub notifications (or runs offline test cases), classifies each item into **URGENT / NEEDS REVIEW / INFORMATIONAL**, ranks them, writes draft replies, and exports `triage_digest.md`. It **never** sends email or posts comments.

**Live demo capture:** [demo/fl07_agent_run_capture.mp4](demo/fl07_agent_run_capture.mp4)  
**Build log:** [build_log.md](build_log.md)

---

## Setup (stranger-friendly)

```bash
git clone https://github.com/ayush0121n/flyrank-ml-assignment.git
cd flyrank-ml-assignment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r personal_agent/requirements.txt
```

Optional live GitHub mode — create `personal_agent/.env` (do **not** commit it):

```
GITHUB_TOKEN=ghp_your_token_with_notifications_scope
```

Without a token the agent runs **offline** with mock cases that match the FL-06/07 spec.

```bash
python personal_agent/agent.py
```

Output: `personal_agent/triage_digest.md` (and console printout).

---

## Usage examples

```bash
# Offline MVP (no secrets)
python personal_agent/agent.py

# With GitHub token in environment
export GITHUB_TOKEN=ghp_xxx
python personal_agent/agent.py
```

Example digest sections:

- **Action items** ranked by priority (CI failures, mentor asks)
- **Inbound drafts** — proposed replies for human send
- **Informational** — PRs and changelogs that need no action

---

## Architecture (simple sketch)

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ GitHub API  │────▶│ Classifier   │────▶│ Digest writer   │
│ or mocks    │     │ (rules/LLM)  │     │ triage_digest.md│
└─────────────┘     └──────────────┘     └─────────────────┘
                           │
                           ▼
                    Draft replies
                    (never auto-sent)
```

- **Ingest:** notifications or fixed test cases  
- **Classify:** keyword/rule tiers (URGENT → REVIEW → INFO)  
- **Act:** write markdown only — human reviews before any outbound action  

---

## Eval results (v2 / MVP)

| Check | Result |
|-------|--------|
| End-to-end run without mid-run hand-edit | Pass (offline + optional API) |
| Live tool connection | GitHub REST notifications when `GITHUB_TOKEN` set |
| Offline fallback | 5 mock items classified + drafts written |
| Safety | No send/post APIs called |
| Output artifact | `triage_digest.md` produced every run |

This is an MVP eval, not a large labeled benchmark: success = complete loop, correct tiers on fixtures, zero accidental outbound actions.

---

## Limitations (honest)

1. **Rule-based classifier** can mis-tier novel notification wording; not a trained NLU model.  
2. **Offline demo is short** — the recorded capture shows the full loop, not a 20-notification production inbox.  
3. **Draft quality** without an LLM key is template-based.  
4. **No calendar/email connectors** in v1 — GitHub only.  
5. **Token in env only** — never commit secrets.

---

## Design decision worth knowing

**Propose, never send.** Drafts are the product. That keeps the agent useful on day one and safe in a portfolio demo.

---

## AI transparency

Portions of scaffolding, docs, and iteration notes were produced **with AI assistance (Grok / pair-programming)**. I defined the job (triage + drafts + no auto-send), ran the agent, verified offline and token paths, and own the safety boundary and build log. AI accelerated typing; it did not replace checking the run or the limitation list.

---

## Demo video notes (for FL-09 recording)

Record 3–5 minutes of the **real terminal run** (not slides):

1. `python personal_agent/agent.py`  
2. Narrate: fetch/classify → ranked items → drafts → file written  
3. On camera: one design decision (**no auto-send**) and one limitation (**rule-based tiers / short offline fixture**)  
4. Optional: open `triage_digest.md`

Existing raw capture: [demo/fl07_agent_run_capture.mp4](demo/fl07_agent_run_capture.mp4) — extend with narration for the showcase thread if needed.
