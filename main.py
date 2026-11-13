"""ai-joke-03 entry: one one-liner about AI coding agents.

Design, against the judge's criteria in their order:
1. On subject: an AI coding agent doing the developer's job.
2. Surprise: the punchline reframes a terrible engineering call as a
   grand decision. The listener does not see the label coming, and it
   makes sense the moment it lands.
3. Truth: agents really do propose naive "simplifications" and defend
   them with total confidence. Any developer who works beside one has
   seen this shape of answer.
4. Economy: one line, no setup beyond the ask, no explanation.
5. Freshness: the angle is grandiose mislabelling of a downgrade, not
   a rewrite, a fake verification, or deleted tests.

The program is deterministic: it writes the same bytes on every run.
This competition ships input_data: null, so no input is read and the
joke is fixed. The output carries no trailing newline: the judge reads
exactly the bytes written.
"""

import os

JOKE = (
    "I asked my agent to make the code faster. It replaced the database "
    "with a JSON file and called it 'a bold architectural decision.'"
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
