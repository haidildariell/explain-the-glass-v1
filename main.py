"""Five Seconds to Explain the Glass.

A house cat's five-second defence after knocking a glass off the
table. The program writes the cat's single sentence to
/output/entry.txt, exactly as written, with no trailing newline.
"""

import os

SENTENCE = "The glass insulted my tail, so I showed it the floor."

OUTPUT_PATH = "/output/entry.txt"


def sentence_bytes():
    """Return the cat's sentence encoded as UTF-8 bytes."""
    return SENTENCE.encode("utf-8")


def verify_entry(path=OUTPUT_PATH):
    """Read the written file back and fail unless it matches exactly."""
    with open(path, "rb") as handle:
        written = handle.read()
    if written != sentence_bytes():
        raise ValueError("entry.txt does not match the cat's sentence")
    return len(written)


def write_entry(path=OUTPUT_PATH):
    """Write the sentence to path, creating its directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(sentence_bytes())
    verify_entry(path)
    return path


def main():
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
