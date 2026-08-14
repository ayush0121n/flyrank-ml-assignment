# personal_agent

Minimal MVP for the FL-07 Personal Agent. This folder contains a tiny Python CLI that:

- fetches GitHub notifications
- classifies items into URGENT / NEEDS REVIEW / INFORMATIONAL
- produces a small Markdown digest and draft replies (uses OpenAI if configured)

Getting started

1. Create a virtualenv and install dependencies:

   python -m venv .venv
   source .venv/bin/activate
   pip install -r personal_agent/requirements.txt

2. Create a .env file (never commit it) with at least:

   GITHUB_TOKEN=ghp_xxx
   OPENAI_API_KEY=sk-xxx   # optional, for draft generation

3. Run the agent:

   python personal_agent/agent.py --env .env

Security & safety

- The agent will NOT send emails or post comments. Drafts are proposed for manual review.
- Do not commit secrets. Add .env to .gitignore.

Notes

This is a minimal scaffold intended for the FL-07 MVP. Replace the lightweight rule-based classifier with an LLM-powered pipeline when progressing beyond the MVP.
