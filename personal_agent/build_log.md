# FL-07 Build Log: DevTriage AI (MVP)

## 1. Platform & Goal
- **Platform:** Scripted Python agent (`personal_agent/agent.py`)
- **Live tool:** GitHub REST API (`/notifications`) via Personal Access Token
- **Core job:** Fetch inbound notifications → classify into URGENT / NEEDS REVIEW / INFORMATIONAL → produce safety-gated draft replies → write `triage_digest.md`
- **Target:** One clean end-to-end run in under 10 hours of build time

## 2. What Broke & What I Changed

### Issue 1 – Empty GitHub inbox during testing
- Fresh tokens often returned `200 OK` with `[]` (no unread notifications).
- **Change:** Added automatic fallback. If the live call returns empty or fails, the agent loads the five realistic test scenarios defined in the FL-06 spec so the demo always has content.

### Issue 2 – LLM dependency made demos fragile
- Early versions required a live Gemini or OpenAI key. When the key was missing or rate-limited the whole run stopped.
- **Change:** Implemented a deterministic offline rule-based classifier + draft generator. The agent still prefers live LLM when keys exist, but the core job never fails without them.

### Issue 3 – Inconsistent markdown headings from LLM
- Raw completions sometimes changed the structure of the digest.
- **Change:** Locked the output format in the system prompt and mirrored the same structure in the offline path so both paths produce identical section headings.

## 3. Scope Cuts from FL-06 Spec (and why)
| Original item              | Decision in MVP                          | Reason |
|---------------------------|------------------------------------------|--------|
| Gmail OAuth 2.0           | Cut                                      | OAuth consent screen + token refresh added too much setup friction for a 10-hour checkpoint |
| SQLite processed-ID cache | Cut → replaced by atomic markdown write  | Zero extra dependency; one file is enough for the demo |
| Auto-sending replies      | Never implemented                        | Safety rule: agent only proposes drafts; human always reviews |

## 4. Verification Against the Five Spec Test Cases
1. Build failure on main → correctly flagged **[URGENT]**
2. Mentor notebook request → produces fill-in draft reply
3. Newsletter → lands in **Informational** summary
4. Vague meeting request → draft offers two concrete time slots
5. PR #14 (15 files) → routed to **[NEEDS REVIEW]**

All five produce the expected categories and draft structure in both live and offline modes.

## 5. Final End-to-End Run (recorded)
- Command: `python personal_agent/agent.py`
- Live tool path: GitHub API call (falls back cleanly when inbox is empty)
- Output: `personal_agent/triage_digest.md` written automatically
- No mid-run hand editing required

## 6. Next Steps (post-MVP)
- Re-introduce Gmail connector once OAuth flow is stable
- Add simple SQLite deduplication of already-triaged notification IDs
- Optional: schedule daily runs via GitHub Actions cron
