#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human right after breaking production. Pure stdlib, deterministic.
"""

import os

# The excuse, built from named parts so each beat can be tuned separately:
# a polite opener, the setup, and the punchline.
OPENER = "In my defence,"
SETUP = "nobody told me the big red 'DROP TABLE' button"
PUNCH = "was load-bearing."

LINE = f"{OPENER} {SETUP} {PUNCH}"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
