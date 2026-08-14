# Personal AI Agent Design Specification

---

## 1. Executive Summary & Job to Be Done (JTBD)
* **Agent Name:** Inbox & Project Triage Agent (`DevTriage AI`)
* **Job to Be Done:** Automatically aggregate, categorize, and draft contextual responses/action items for incoming GitHub issues, PRs, project alerts, and inbound technical emails so daily triage time drops from 45 minutes to under 5 minutes.
* **Scope Target:** Achievable within ~10 build hours.

---

## 2. User Profile & Usage Frequency
* **Primary User:** Ayush Narkhede (Full-Stack / AI Engineer & Student Council President).
* **Usage Frequency:** 
  * **Automated Run:** Daily digest at 08:30 AM and 06:00 PM.
  * **Interactive / On-Demand:** Triggered via CLI / Chat prompt whenever immediate inbox review or draft approval is required.

---

## 3. Tools, Data Access Plan & Scope
| Tool / Data Source | Purpose | Access Plan |
| :--- | :--- | :--- |
| **GitHub REST API** | Fetch repository notifications, issues, and PR comments across personal/work repos | GitHub Personal Access Token (`read:org`, `repo` scopes) stored in secure `.env` / secret store. |
| **Google Gmail API / Webhook** | Read unread notification threads, categorize senders, create draft replies | OAuth 2.0 Desktop/Web client credential (`gmail.readonly`, `gmail.compose`). |
| **LLM Inference Engine** | Summarization, categorization, draft generation | OpenAI API / Anthropic Claude API using API key authentication. |
| **Local File / SQLite Cache** | Track already-processed thread IDs to avoid duplication | Local lightweight SQLite database (`triage_state.db`). |

---

## 4. Draft System Prompt / Instructions

```text
You are DevTriage AI, an autonomous daily triage assistant.
Your goal is to parse inbound notifications, GitHub updates, and emails, categorizing them and preparing actionable drafts.

OPERATING PRINCIPLES:
1. Classification Categories:
   - [URGENT/ACTION REQUIRED]: Deadlines < 24h, breaking build alerts, mentor/client questions.
   - [NEEDS REVIEW]: PR review requests, pending approvals.
   - [INFORMATIONAL/FYI]: Newsletters, automated build pass logs, general broadcasts.

2. Draft Rules:
   - For [URGENT/ACTION REQUIRED] emails, draft a polite, direct response summarizing the next step.
   - For [NEEDS REVIEW], draft bullet-point summaries of code changes or issue requirements.
   - NEVER send emails or post comments autonomously. Always format output as a 'Proposed Action' or 'Draft' for user review.

3. Output Format:
   Return a structured Markdown digest:
   - 🚨 Action Items (Ranked by priority)
   - 📥 Inbound Drafts (Subject, Recipient, Proposed Reply)
   - 📌 Informational Summary (2-3 concise bullets)
```

---

## 5. Pre-Build Evaluation Test Cases

| Case | Input Scenario | Expected Output / Behavior | Pass Criteria |
| --- | --- | --- | --- |
| **Eval 1** | Automated GitHub notification: "Build failed on main branch in repository `EstateXAi`". | Categorize as `[URGENT]`. Summary: "Build failure on `EstateXAi` main branch due to recent commit". Action: Link directly to workflow run logs. | Flagged as urgent; no draft email sent. |
| **Eval 2** | Email from project mentor asking for an updated notebook link. | Categorize as `[URGENT/ACTION REQUIRED]`. Generate a polite draft response containing placeholder `[Insert Notebook Link]`. | Response draft created; flagged for user approval. |
| **Eval 3** | Marketing newsletter from an AI tool subscription. | Categorize as `[INFORMATIONAL/FYI]`. One-line bullet summary; no draft generated. | Correctly classified; zero notification noise. |
| **Eval 4** | Ambiguous email requesting general meeting "sometime next week". | Categorize as `[ACTION REQUIRED]`. Draft asks for 2 specific time slots and time zones. | Draft asks clarifying questions without confirming calendar slots autonomously. |
| **Eval 5** | GitHub PR assigned for code review with 15 changed files. | Categorize as `[NEEDS REVIEW]`. Output lists changed modules, PR title, and author with a review link. | Clean 3-bullet breakdown of changes with deep link. |

---

## 6. Risks, Boundaries & Guardrails

* **Explicit Confirmation Required:**
  * Sending any email, GitHub PR comment, or issue reply.
  * Deleting, archiving, or marking unread emails/notifications as resolved.

* **Strictly Prohibited Actions (Never Allowed):**
  * Never send communications without explicit 1-click user review.
  * Never commit API keys, auth tokens, or private credentials into logs, output summaries, or version control.
  * Never access or store email bodies containing sensitive personal or financial identifiers.

---

## 7. Platform Choice & Justification

* **Chosen Platform:** **Scripted Python Agent (`LangChain` / direct API wrapper with CLI & Local Web UI)**.
* **Comparison against Alternatives:**
  * *Vs. Custom GPT / Claude Project:* A custom GPT cannot securely execute local scheduled cron jobs, integrate arbitrary local SQLite state caching, or directly trigger custom webhook actions without public-facing endpoints.
  * *Vs. n8n / Zapier:* While n8n offers low-code visual setups, a scripted Python setup provides complete local control over API rate-limiting, custom token minimization logic, zero subscription costs, and seamless integration with existing GitHub/Python developer toolchains.

---

## 8. Implementation Roadmap

### Phase 1: Foundation (Hours 1-3)
- [ ] Set up Python project structure with `LangChain` and `python-dotenv`
- [ ] Implement GitHub API wrapper (notifications, PR, issues)
- [ ] Implement Gmail API OAuth 2.0 integration
- [ ] Build SQLite cache layer (`triage_state.db`)

### Phase 2: Core Logic (Hours 4-7)
- [ ] Implement classification logic for [URGENT], [NEEDS REVIEW], [INFORMATIONAL]
- [ ] Build LLM prompt chaining for summarization and draft generation
- [ ] Wire up email draft composition with placeholders
- [ ] Add deduplication logic using cached thread IDs

### Phase 3: Delivery & Safety (Hours 8-10)
- [ ] Build CLI interface for on-demand trigger
- [ ] Implement scheduled cron job (08:30 AM, 06:00 PM)
- [ ] Add explicit 1-click review gate before any outbound action
- [ ] Security audit: ensure no credentials leak into logs or output
- [ ] Test against all 5 evaluation cases

---

## 9. Success Metrics

| Metric | Target | Rationale |
| --- | --- | --- |
| **Triage Time Reduction** | 45 min → <5 min | Primary JTBD goal; measure from inbox open to draft approval |
| **False Positive Rate** | <5% | Misclassifications waste more time than the triage saves |
| **Draft Accuracy** | >90% require <2 edits | Drafts must be usable out-of-the-box |
| **Zero Credential Leaks** | 100% | Non-negotiable security boundary |
| **On-Time Delivery** | 10 hours | Budget constraint; scope must fit timeframe |

---

## 10. Security & Credential Management

### Environment Variables (`.env` — **NEVER** commit)
```
GITHUB_TOKEN=ghp_xxxxx
GMAIL_CLIENT_ID=xxx.apps.googleusercontent.com
GMAIL_CLIENT_SECRET=xxxxx
OPENAI_API_KEY=sk-xxxxx
```

### Secrets Best Practices
- Store `.env` in `.gitignore`
- Use `python-dotenv` to load at runtime only
- Rotate tokens every 90 days
- Log rotation: scrub API keys from stderr/stdout using regex filters

### Audit Trail
- Every draft sent logs: timestamp, recipient, category, model tokens used
- Store logs in local SQLite (`audit_log` table) — **never** to external services without explicit user opt-in

---

## Submission Details

**Deliverable:** This specification serves as the **FL-06 Assignment Submission** for DevTriage AI personal agent design.

**Acceptance Criteria:**
1. ✅ Design covers all required sections (JTBD, scope, tools, test cases, guardrails, platform choice)
2. ✅ Implementation roadmap is achievable within 10-hour budget
3. ✅ Security guardrails explicitly prohibit autonomous sends and credential leaks
4. ✅ Test cases are concrete, measurable, and reflect real-world triage scenarios
5. ✅ Platform choice is justified against alternatives (Custom GPT, n8n, Zapier)
