# -*- coding: utf-8 -*-
import tempfile
from os.path import basename, splitext, exists, join
from mobi.kindleunpack import unpackBook


def extract(infile):
    """Extract mobi file and return path to epub file"""
    fname_in = basename(infile)
    base, ext = splitext(fname_in)
    fname_out = base + ".epub"
    tempdir = tempfile.mkdtemp(prefix="mobiex")
    unpackBook(infile, tempdir, epubver="A")
    epub_filepath = join(tempdir, "mobi8", fname_out)
    assert exists(epub_filepath)
    return tempdir, epub_filepath


if __name__ == "__main__":
    print(extract("../tests/demo.mobi"))
