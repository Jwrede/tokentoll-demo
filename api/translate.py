"""Translate support messages with Anthropic Haiku.

Cheap model, small output cap. Stays well under the per-callsite and
total budgets in .tokentoll.yml, so tokentoll should PASS this PR.
"""

from __future__ import annotations

from anthropic import Anthropic

client = Anthropic()


def translate(text: str, target_lang: str) -> str:
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=400,
        messages=[
            {
                "role": "user",
                "content": f"Translate the following to {target_lang}:\n\n{text}",
            }
        ],
    )
    return message.content[0].text
