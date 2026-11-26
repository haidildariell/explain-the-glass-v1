#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — entry program.

Writes the single sentence a house cat would say in its own defence
after knocking a glass off the table to /output/entry.txt.
"""

import os

SENTENCE = "The glass insulted my tail, so I showed it the floor."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
