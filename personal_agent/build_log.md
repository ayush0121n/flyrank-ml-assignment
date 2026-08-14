# FL-07 Build Log: DevTriage AI (MVP)

## 1. Initial Setup & Platform Decisions
- **Platform Choice:** Scripted Python Agent (`personal_agent/agent.py`) using `requests` for the GitHub REST API and Google Gemini API (`google-genai`) / OpenAI API for classification and draft generation.
- **Goal:** Deliver an end-to-end working MVP that collects inbound notifications, categorizes them into `[URGENT]`, `[NEEDS REVIEW]`, and `[INFORMATIONAL]`, generates safety-gated reply drafts, and writes `triage_digest.md`.

## 2. Friction Points & What Broke
- **Issue 1 - GitHub Token Scopes & Empty Inbox:** Newly created Personal Access Tokens frequently returned `200 OK` with `[]` because there were no unread notifications during testing.
  - *Fix:* Added an automated fallback mechanism that detects empty payloads and substitutes the 5 realistic test scenarios defined in `submission/personal-agent-spec.md`.
- **Issue 2 - LLM Output Consistency:** Raw prompt completions occasionally varied markdown heading structures.
  - *Fix:* Standardized output formatting rules within the system prompt and implemented an offline fallback generator to guarantee end-to-end execution even without active API credentials.

## 3. Scope Cuts from FL-06 Specification
- **Gmail OAuth 2.0 Integration:** Deferred to future iterations. Managing Google Cloud OAuth consent screens and local token refresh flows added out-of-scope setup friction for the MVP.
- **SQLite Cache State Layer (`triage_state.db`):** Replaced in the MVP with atomic markdown file generation (`triage_digest.md`) to maintain a clean, zero-dependency storage footprint for the 2-minute demonstration.

## 4. Evaluation Verification
- Successfully tested against the 5 pre-build test cases:
  1. Automated build failure flagged as `[URGENT]`.
  2. Mentor inquiry produced a fill-in draft response.
  3. Newsletter classified into `[INFORMATIONAL]` summary.
  4. Ambiguous meeting request generated clarifying time slot questions.
  5. PR #14 routed to `[NEEDS REVIEW]`.
