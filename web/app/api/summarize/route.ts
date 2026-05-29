import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const { conversation } = await req.json();

  const { text } = await generateText({
    model: openai("gpt-4o-mini"),
    maxOutputTokens: 200,
    prompt: `Summarize this support conversation in one sentence:\n${conversation}`,
  });

  return NextResponse.json({ summary: text });
}
