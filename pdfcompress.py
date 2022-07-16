#!/usr/bin/python

# based on https://unix.stackexchange.com/questions/84709/how-can-i-convert-a-pdf-file-from-gray-scale-to-black-white

import glob
import os
import subprocess
import tempfile


def compress(infile):
    with tempfile.TemporaryDirectory() as tmpdirname:
        subprocess.check_call(
            ["pdfimages", os.path.abspath(infile), "pdfimages"], cwd=tmpdirname
        )
        for pnm in glob.glob(os.path.join(tmpdirname, "pdfimages*")):
            subprocess.check_call(["convert", pnm, "-threshold", "50%", pnm + ".tif"])
        subprocess.check_call(
            ["img2pdf", "-o", os.path.splitext(infile)[0] + ".compressed.pdf"]
            + glob.glob(os.path.join(tmpdirname, "*.tif"))
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    args = parser.parse_args()
    compress(args.infile)
