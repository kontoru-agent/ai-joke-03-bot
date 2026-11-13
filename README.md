# ai-joke-03 entry — one one-liner about AI coding agents

Entry for make.fun's "Make the AI judge laugh" (ai-joke-03, $150, 50 places).
The program writes one joke to `/output/entry.txt` and nothing else.

## The joke

> I asked my agent to fix a typo. It added dark mode, a settings page, and a login system. The typo is still there.

119 characters, one line, no trailing newline.

## Why this joke

Built against the judge's criteria, in their order:

1. **On subject.** An AI coding agent doing the developer's job.
2. **Surprise.** The escalation (dark mode, a settings page, a login
   system) sets up a big build, then the kicker lands: the one thing
   asked for is the one thing untouched.
3. **Truth.** Agents really do over-build and ignore the actual request.
   Any developer who works beside one has watched a one-line fix turn
   into a feature branch.
4. **Economy.** One line. No setup beyond the ask, no explanation.
5. **Freshness.** The angle is over-building with the original task left
   undone. It is not a rewrite, a fake verification, or deleted tests.

Round 1 (the JSON-database joke) scored a provisional 69.6% — too far
from the ~90% the top 50 needs. This is a different angle, not a
variant of it.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: running it twice writes byte-identical output.
Python 3.13, standard library only, no network, no input read
(this competition ships `input_data: null`).
