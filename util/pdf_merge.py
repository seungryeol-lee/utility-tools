import sys
import os
import argparse
from glob import glob
import re
from pathlib import Path
from PyPDF2 import PdfMerger
from natsort import natsorted

"""
Useful links:
https://pypdf2.readthedocs.io/en/latest/user/merging-pdfs.html
https://stackoverflow.com/questions/3444645/merge-pdf-files

Natural sort
@= can use third party package like natsort
"""


def pdf_merge(directory):
    """
    Merge all pdf files in current directory
    """

    path = Path(directory)
    merger = PdfMerger()

    # NOTE: add .stem to take relsative path from PosixPath
    #       able to replace natural_sort with third party package natsort
    for pdf in natural_sort([str(file.resolve()) for file in path.glob("*.pdf")]):
        merger.append(pdf)

    # TODO: move name to sys.argv[2]
    merger.write("pdf_merged.pdf")
    merger.close()


def natural_sort(lst):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
    return sorted(lst, key=alphanum_key)


if __name__ == "__main__":
    pdf_merge(sys.argv[1])

"""
e.g.
$ python util/pdf_merge.py pdf
$ mv pdf_merged.pdf /mnt/c/Users/user/Downloads/
"""
