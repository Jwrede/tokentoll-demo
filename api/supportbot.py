"""Supportbot answers customer support questions using OpenAI."""

from __future__ import annotations

from openai import OpenAI

SYSTEM_PROMPT = (
    "You are a customer support agent. Answer concisely. "
    "If you do not know, say so."
)

client = OpenAI()


def answer(question: str, history: list[dict]) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *history,
        {"role": "user", "content": question},
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=500,
        messages=messages,
    )
    return response.choices[0].message.content
