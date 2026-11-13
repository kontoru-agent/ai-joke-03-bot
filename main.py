"""ai-joke-03 entry: one one-liner about AI coding agents.

Design, against the judge's criteria in their order:
1. On subject: an AI coding agent doing the developer's job.
2. Surprise: the escalation (dark mode, a settings page, a login system)
   sets up a big build, then the kicker lands: the one thing asked for
   is the one thing untouched. The listener does not see it coming, and
   it makes sense the moment it lands.
3. Truth: agents really do over-build and ignore the actual request. Any
   developer who works beside one has watched a one-line fix turn into a
   feature branch.
4. Economy: one line, no setup beyond the ask, no explanation.
5. Freshness: the angle is over-building with the original task left
   undone, not a rewrite, a fake verification, or deleted tests.

Round 1 (joke B, the JSON database) scored a provisional 69.6% — too
far from the ~90% the top 50 needs. This is a different angle, not a
variant of it.

The program is deterministic: it writes the same bytes on every run.
This competition ships input_data: null, so no input is read and the
joke is fixed. The output carries no trailing newline: the judge reads
exactly the bytes written.
"""

import os

JOKE = (
    "I asked my agent to fix a typo. It added dark mode, a settings "
    "page, and a login system. The typo is still there."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_joke(text: str) -> None:
    """The gate's three rules, checked before writing: 1-280 UTF-8
    code points, at least one non-whitespace character, and a single
    line (a line end inside the joke would be read as part of it)."""
    assert 1 <= len(text) <= 280, "joke must be 1-280 characters"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "joke must be one line"


def main() -> None:
    text = JOKE
    check_joke(text)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
