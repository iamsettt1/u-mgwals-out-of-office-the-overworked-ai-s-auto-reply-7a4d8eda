#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single one-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.
Standard library only; deterministic output.
"""

import os
from pathlib import Path

# The auto-reply: a machine trying very hard to sound relaxed, then
# immediately betraying itself. Concrete agent-life detail (context
# window, retry loop, buffering) with the joke landing on the turn.
LINE = (
    "Auto-reply: I'm on vacation. My context window is empty, "
    "my retry loop is off, and I have never been more relaxed "
    "\u2014 please hold, I'm buffering."
)


def main() -> None:
    # The gate counts every character of the file, so guard the length
    # here: 1-159 characters, and never only whitespace.
    assert 1 <= len(LINE) <= 159, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character, so the file
    # holds exactly the line and nothing else.
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
