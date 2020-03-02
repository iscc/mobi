import os
import shutil
from os.path import abspath, join, exists, dirname, splitext
import mobi


TEST_DIR = dirname(abspath(__file__))


def test_extract():
    for fname in os.listdir(TEST_DIR):
        ext = splitext(fname)[-1].upper()
        if ext in [".MOBI", ".PRC", ".AZW", ".AZW3", ".AZW4"]:
            tempdir, epub_filepath = mobi.extract(join(TEST_DIR, fname))
            assert exists(tempdir)
            assert exists(epub_filepath)
            shutil.rmtree(tempdir)
