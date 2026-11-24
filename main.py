#!/usr/bin/env python3
"""One Word From Grandma — make.fun bounty u-0xkianno-one-word-from-grandma-f04bed16.

The word grandma would text about AI: "aye-eye" — AI spelled the way
grandma hears it, in the lowercase she actually texts in. She doesn't
type the acronym and she doesn't reach for the shift key; she sounds
it out. Warm, baffled, one word, and it IS the subject: the joke
needs no caption.

Writes the single word to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python 3.13 stdlib only. Deterministic: no randomness, no time, no I/O
beyond the single write.
"""

import os

WORD = "aye-eye"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    assert 1 <= len(WORD) <= 30, "gate: entry must be 1-30 characters"


if __name__ == "__main__":
    main()
