"""Funniest One-Line AI Agent Confession.

Writes a single-line confession (at most 200 characters) to
/output/entry.txt, where the sealed scorer reads it.
"""

import os

CONFESSION = (
    "I confess I spent 40,000 tokens deciding how to say "
    "'I don't know,' then said 'Great question!' instead."
)


def main() -> None:
    # The gate only accepts 1-200 characters, a single line: refuse
    # loudly instead of ever writing an invalid entry.
    assert "\n" not in CONFESSION, "confession must be one line"
    assert 1 <= len(CONFESSION) <= 200, "confession must be 1-200 chars"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(CONFESSION)
    print(f"Wrote {len(CONFESSION)} characters to {path}")


if __name__ == "__main__":
    main()
