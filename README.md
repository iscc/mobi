# mobi - library for unpacking mobi files

[![Version](https://img.shields.io/pypi/v/mobi.svg)](https://pypi.python.org/pypi/mobi/)
[![Downloads](https://pepy.tech/badge/mobi)](https://pepy.tech/project/mobi)

> A fork of [KindleUnpack](https://github.com/kevinhendricks/KindleUnpack) which removes the GUI part and makes it available as a python library via [PyPi](https://pypi.org/project/mobi/) for easy unpacking of mobi files.

## Usage

```python
import mobi

tempdir, epub_filepath = mobi.extract("mybook.mobi")
```

| NOTE: You are responsible to delete the generated tempdir! |
| --- |
