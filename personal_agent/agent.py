"""
Minimal Personal Agent MVP (FL-07)

This module provides a lightweight CLI to fetch GitHub notifications, classify them,
and produce a small Markdown digest and proposed drafts. It is intentionally
minimal and safe: it will not send emails or post comments.

Dependencies: requests, python-dotenv, openai (optional), google-genai (optional)
"""

import os
import sys
import json
import argparse
from datetime import datetime
from dotenv import load_dotenv

try:
    import requests
except Exception:
    requests = None

# Optional model clients
try:
    import openai
except Exception:
    openai = None

try:
    import google_genai
except Exception:
    google_genai = None


GITHUB_NOTIFICATIONS_URL = "https://api.github.com/notifications"


def load_env(path: str = ".env"):
    load_dotenv(path)


def fetch_github_notifications(token: str, per_page: int = 50):
    """Fetch recent notifications from the GitHub REST API.
    Returns a list of simplified notification dicts.
    """
    if requests is None:
        raise RuntimeError("requests library is required")
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    params = {"all": "false", "per_page": per_page}
    resp = requests.get(GITHUB_NOTIFICATIONS_URL, headers=headers, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    simplified = []
    for n in data:
        simplified.append({
            "id": n.get("id"),
            "repository": n.get("repository", {}).get("full_name"),
            "title": n.get("subject", {}).get("title"),
            "type": n.get("subject", {}).get("type"),
            "url": n.get("subject", {}).get("url"),
            "reason": n.get("reason"),
            "updated_at": n.get("updated_at"),
        })
    return simplified


def classify_item(title: str, typ: str, reason: str) -> str:
    """Very small rule-based classifier for triage categories."""
    text = " ".join(filter(None, [title, typ, reason])).lower()
    urgent_keywords = ["failed", "failure", "error", "urgent", "critical", "breaking", "downtime"]
    review_keywords = ["review", "pr", "pull request", "requested", "r?e?view"]
    for k in urgent_keywords:
        if k in text:
            return "URGENT/ACTION REQUIRED"
    for k in review_keywords:
        if k in text:
            return "NEEDS REVIEW"
    return "INFORMATIONAL/FYI"


def generate_draft_with_openai(subject: str, summary: str) -> str:
    if openai is None:
        return f"[DRAFT PLACEHOLDER] Subject: {subject}\n\nSummary:\n{summary}\n\n(Install openai and set OPENAI_API_KEY to generate a better draft.)"
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return f"[DRAFT PLACEHOLDER] Subject: {subject}\n\nSummary:\n{summary}\n\n(No OPENAI_API_KEY found.)"
    openai.api_key = api_key
    prompt = (
        f"You are a concise engineering assistant. Given the subject: {subject} and summary: {summary},"
        " write a short polite draft reply (2-5 sentences) with suggested next steps."
    )
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.2,
        )
        return resp["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[DRAFT ERROR] Could not call OpenAI: {e}"


def generate_digest(items):
    digest = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "action_items": [],
        "drafts": [],
        "informational": [],
    }
    for it in items:
        cat = classify_item(it.get("title", ""), it.get("type", ""), it.get("reason", ""))
        summary = f"[{it.get('repository')}] {it.get('title')} (type={it.get('type')})"
        entry = {"id": it.get("id"), "repo": it.get("repository"), "title": it.get("title"), "category": cat, "summary": summary, "updated_at": it.get("updated_at"), "url": it.get("url")}
        if cat == "URGENT/ACTION REQUIRED":
            digest["action_items"].append(entry)
            draft = generate_draft_with_openai(it.get("title", ""), summary)
            digest["drafts"].append({"for": it.get("id"), "subject": it.get("title"), "draft": draft})
        elif cat == "NEEDS REVIEW":
            digest["action_items"].append(entry)
            draft = generate_draft_with_openai(it.get("title", ""), summary)
            digest["drafts"].append({"for": it.get("id"), "subject": it.get("title"), "draft": draft})
        else:
            digest["informational"].append(entry)
    return digest


def print_markdown(digest):
    print(f"# Personal Agent Digest — Generated {digest.get('generated_at')}")
    print()
    if digest["action_items"]:
        print("## 🚨 Action Items")
        for idx, a in enumerate(digest["action_items"], 1):
            print(f"{idx}. **{a['repo']}** — {a['title']} — {a['category']}")
            if a.get("url"):
                print(f"   - Link: {a['url']}")
            print(f"   - Updated: {a.get('updated_at')}")
        print()
    if digest["drafts"]:
        print("## 📥 Inbound Drafts")
        for d in digest["drafts"]:
            print(f"### Draft for {d['subject']}")
            print(d["draft"]) 
            print()
    if digest["informational"]:
        print("## 📌 Informational Summary")
        for info in digest["informational"]:
            print(f"- {info['repo']}: {info['title']}")
    print()
    print("---")
    print("Note: This agent never sends messages automatically. Review drafts before any outbound action.")


def main():
    parser = argparse.ArgumentParser(description="Run the minimal personal agent digest generator.")
    parser.add_argument("--env", default=".env", help="Path to .env file")
    parser.add_argument("--github-token", default=None, help="GitHub token (overrides GITHUB_TOKEN in .env)")
    args = parser.parse_args()

    load_env(args.env)
    token = args.github_token or os.getenv("GITHUB_TOKEN")
    if not token:
        print("No GITHUB_TOKEN found. Exiting. Set GITHUB_TOKEN in your environment or pass --github-token.")
        sys.exit(1)
    try:
        items = fetch_github_notifications(token)
    except Exception as e:
        print(f"Failed to fetch GitHub notifications: {e}")
        sys.exit(1)
    digest = generate_digest(items)
    print_markdown(digest)


if __name__ == "__main__":
    main()
