# tokentoll-demo

Live demo for [tokentoll](https://github.com/Jwrede/tokentoll). A tiny polyglot LLM app (Python + TypeScript) wired up to tokentoll's CI cost gate.

## What's here

- `api/supportbot.py` -- Python backend that answers support questions via OpenAI.
- `web/app/api/summarize/route.ts` -- Next.js edge route that summarizes conversations via the Vercel AI SDK.
- `.tokentoll.yml` -- the policy. Budgets are intentionally tight so model regressions trip the gate.
- `.github/workflows/tokentoll.yml` -- runs tokentoll on every PR, fails the workflow on policy violations.

## Two example PRs

- A passing PR: adds a cheap Anthropic call for translation. tokentoll detects the new call site and PASSes because it stays under all budgets.
- A failing PR: swaps `gpt-4o-mini` to `gpt-4o` on an existing call site. The 15x per-call cost jump trips `max_relative_increase` and tokentoll posts a FAIL verdict that blocks the merge.

Open the PR conversation tab on either to see the verdict comment tokentoll posts.

## Policy

```yaml
budgets:
  max_monthly_delta_usd: 100
  max_callsite_monthly_usd: 50
  max_relative_increase: 5.0

policies:
  fail_on_policy_violation: true
```

See [tokentoll/docs/policy.md](https://github.com/Jwrede/tokentoll/blob/main/docs/policy.md) for the full schema.
