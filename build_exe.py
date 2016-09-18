#!/usr/bin/python2

import os
import sys
import time
import getopt
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "sys", "time", "getopt"]}

includes = ["sys", "os", "time", "getopt"]

setup(name='batch-renamer-cli', version='1.0.2b', description='Batch rename files in a folder quickly.', options = {"build_exe": {"includes":includes}}, executables= [Executable("batch-renamer-cli.py")])
