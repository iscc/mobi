import shutil
from os.path import abspath, join, exists, dirname
import mobi


TEST_DIR = dirname(abspath(__file__))


def test_extract():
    tempdir, epub_filepath = mobi.extract(join(TEST_DIR, "demo.mobi"))
    assert exists(tempdir)
    assert exists(epub_filepath)
    shutil.rmtree(tempdir)
