#!/usr/bin/env python3
"""Write the six-word story to /output/entry.txt.

The story: "Our robot vacuum filed for custody."
Six words, one domestic absurdity with a turn: the machine that was
bought to clean the house has become family enough to sue for it.
It stands apart from the field's grief/forgiveness/letter cluster —
a funny, AI-adjacent story instead of another funeral.
"""

import os

STORY = "Our robot vacuum filed for custody."


def write_entry(story):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(story)


def main():
    write_entry(STORY)


if __name__ == "__main__":
    main()
