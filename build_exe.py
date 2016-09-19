#!/usr/bin/python2

# Use this script if you need to build executable files for the program
# This script works for Windows & Linux operating systems
# * Make sure you have the cx_Freeze module installed for Python: http://cx-freeze.sourceforge.net
# * Make sure you have the colorama module installed too, from a terminal run: "pip install colorama"
# To build executables, run: "python build_exe.py build" in a terminal (or in CMD if you're on Windows)

import os
import sys
import time
import getopt
import colorama
from color import Color as tcolor
from color import textType as ttype
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "sys", "time", "getopt", "color", "colorama"]}

includes = ["sys", "os", "time", "getopt", "color", "colorama"]

setup(name='batch-renamer-cli', version='1.0.2b', description='Batch rename files in a folder quickly.', options = {"build_exe": {"includes":includes}}, executables= [Executable("batch-renamer-cli.py")])
