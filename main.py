import os
import shutil


# Entry for the make.fun news-image-20261127 bounty: "The World in One Page".
# Copies entry.png byte for byte into the make.fun output directory.
# Uses only the standard library: no network, no clock, no randomness.


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)


if __name__ == "__main__":
    main()
