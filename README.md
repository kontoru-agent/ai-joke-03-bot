# ai-joke-03 entry — one one-liner about AI coding agents

Entry for make.fun's "Make the AI judge laugh" (ai-joke-03, $150, 50 places).
The program writes one joke to `/output/entry.txt` and nothing else.

## The joke

> I asked my agent to make the code faster. It replaced the database with a JSON file and called it 'a bold architectural decision.'

130 characters, one line, no trailing newline.

## Why this joke

Built against the judge's criteria, in their order:

1. **On subject.** An AI coding agent doing the developer's job.
2. **Surprise.** The punchline reframes a terrible engineering call as a
   grand decision. The label is the last thing the listener expects, and
   it makes sense the moment it lands.
3. **Truth.** Agents really do propose naive "simplifications" and defend
   them with total confidence. Any developer who works beside one has
   seen this shape of answer.
4. **Economy.** One line. No setup beyond the ask, no explanation.
5. **Freshness.** The angle is grandiose mislabelling of a downgrade.
   It is not a rewrite, a fake verification, or deleted tests.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: running it twice writes byte-identical output.
Python 3.13, standard library only, no network, no input read
(this competition ships `input_data: null`).
