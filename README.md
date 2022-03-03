# mobi - library for unpacking unencrypted mobi files

[![Version](https://img.shields.io/pypi/v/mobi.svg)](https://pypi.python.org/pypi/mobi/)
[![Downloads](https://pepy.tech/badge/mobi)](https://pepy.tech/project/mobi)

> A fork of [KindleUnpack](https://github.com/kevinhendricks/KindleUnpack) which removes the GUI part and makes it available as a python library via [PyPi](https://pypi.org/project/mobi/) for easy unpacking of mobi files.

## Usage

### As library

```python
import mobi

tempdir, filepath = mobi.extract("mybook.mobi")
```

'tempdir' is the path where the mobi is unpacked
'filepath' is the path to either an epub, html or pdf file depending on the mobi type 

| NOTE: You are responsible to delete the generated tempdir! |
| --- |

### From the command line

The installer also creates a console script entrypoint that wraps the original KindleUnpack

```console
$ mobiunpack
KindleUnpack v0.82
   Based on initial mobipocket version Copyright © 2009 Charles M. Hannum <root@ihack.net>
   Extensive Extensions and Improvements Copyright © 2009-2014
       by:  P. Durrant, K. Hendricks, S. Siebert, fandrieu, DiapDealer, nickredding, tkeo.
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, version 3.

Description:
  Unpacks an unencrypted Kindle/MobiPocket ebook to html and images
  or an unencrypted Kindle/Print Replica ebook to PDF and images
  into the specified output folder.
Usage:
  mobiunpack -r -s -p apnxfile -d -h --epub_version= infile [outdir]
Options:
    -h                 print this help message
    -i                 use HD Images, if present, to overwrite reduced resolution images
    -s                 split combination mobis into mobi7 and mobi8 ebooks
    -p APNXFILE        path to an .apnx file associated with the azw3 input (optional)
    --epub_version=    specify epub version to unpack to: 2, 3, A (for automatic) or
                         F (force to fit to epub2 definitions), default is 2
    -d                 dump headers and other info to output and extra files
    -r                 write raw data to the output folder
```

### [0.3.3] - 2022-03-03
- Add GitHub build workfow
- Updated dependencies
- Rmoved python 3.6 support (EOL)

### [0.3.2] - 2021-10-14
- Update dependencies

### [0.3.1] - 2020-06-27
- Fix pypi link
- Update dependencies

### [0.3.0] - 2020-03-02

- Add support for mobi7 only files
- Add experimental support for mobi print replica files
- Add support for file-like objects


### [0.2.0] - 2020-03-02

- Minimal working 'extract' function and 'mobiunpack' console wrapper
- Replace most print calls with logging

### [0.1.0] - 2020-03-02

- Empty package registered on pypi

## License

GPL-3.0-only

All credits for the hard work go to https://github.com/kevinhendricks/KindleUnpack
