# -*- coding: utf-8 -*-
from loguru import logger
import tempfile
from os.path import basename, splitext, exists, join
from mobi.kindleunpack import unpackBook


def extract(infile):
    """Extract mobi file and return path to epub file"""
    # TODO support file-like objects
    fname_in = basename(infile)
    base, ext = splitext(fname_in)
    fname_out_epub = base + ".epub"
    fname_out_html = "book.html"
    fname_out_pdf = base + ".001.pdf"
    tempdir = tempfile.mkdtemp(prefix="mobiex")
    logger.debug("tempdir: %s" % tempdir)
    unpackBook(infile, tempdir, epubver="A")
    epub_filepath = join(tempdir, "mobi8", fname_out_epub)
    html_filepath = join(tempdir, "mobi7", fname_out_html)
    pdf_filepath = join(tempdir, fname_out_pdf)
    if exists(epub_filepath):
        return tempdir, epub_filepath
    elif exists(html_filepath):
        return tempdir, html_filepath
    elif exists(pdf_filepath):
        return tempdir, pdf_filepath
    raise ValueError("Coud not extract from %s" % infile)


if __name__ == "__main__":
    print(extract("../tests/demo.mobi"))
