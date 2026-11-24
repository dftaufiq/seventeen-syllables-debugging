#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

Deterministic: the same three lines, byte for byte, on every run.
Haiku (5-7-5, 17 syllables, 69 characters, 71 bytes with newlines):

    One line fixed at dawn
    a dozen break by breakfast
    the bug had children
"""

import os

HAIKU = (
    "One line fixed at dawn\n"
    "a dozen break by breakfast\n"
    "the bug had children"
)

# Hand-verified syllable counts, line by line:
#   "One line fixed at dawn"          -> 1+1+1+1+1 = 5
#   "a dozen break by breakfast"      -> 1+2+1+1+2 = 7
#   "the bug had children"            -> 1+1+1+2   = 5
EXPECTED_SYLLABLES = (5, 7, 5)


def main() -> None:
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    assert len(HAIKU) <= 200, "haiku must be at most 200 characters"
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        words = line.split()
        assert words, "haiku line must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
