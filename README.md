## Batch Renamer 
[![Build Status](https://travis-ci.org/darko3/batch-renamer.svg?branch=master)](https://travis-ci.org/darko3/batch-renamer) [![Packagist](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org) [![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](https://github.com/darko3/batch-renamer/blob/master/LICENSE) [![Packagist](https://img.shields.io/badge/OS-Linux%20|%20Windows-orange.svg)](#)

![alt text](http://i.imgur.com/aI21hNY.png "Screenshot from v1.0.4")


An easy to use python script for quickly renaming multiple files ending with incrementing numbers.

## Usage
```
Batch File Renamer 1.0.4 - (C) 2017 Girish Oemrawsingh
View this project on Github: https://github.com/darko3/batch-renamer


usage: ./batch-rename.py --folder-path <folder-path> --new-name <new-file-name> [options]

Required:

  -p, --folder-path <folder-path>   specify folder path that includes files to rename
  -n, --new-name <new-file-name>    specify the new filename for the files in the folder

Options:

  -h, --help                        print this help menu and exit
  -V, --version                     print the Batch Renamer version number and exit
  -v, --verbose                     enable verbose output mode
  -s, --suppress-warnings           don't show warning prompt before renaming files
  -e, --ends-with <string>          specify a string to end file names with (useful for file extensions)
```

## Installation

1. Clone the git repository

    `$ git clone https://github.com/darko3/batch-renamer.git`

2. Change directory into the git repository

    `$ cd batch-renamer`

3. Run setup.py

    `$ sudo python setup.py install`

4. If all the above commands were successful, you should now be able to run the script from the commandline

    `$ batch-rename`

## Requirements

* Python 2.x - 3.x
* Colorama module

You can install colorama with `$ sudo pip install colorama`.

## License
This project is licensed under the terms of the MIT license.

You can find and view the license file located in the Github Repository [here](https://github.com/darko3/batch-renamer/blob/master/LICENSE).

<!-- https://docs.travis-ci.com/user/languages/python -->
<!-- https://shields.io -->
