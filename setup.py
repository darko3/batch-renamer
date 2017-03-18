#!/usr/bin/python

import os
import shutil
from distutils.core import setup

if not os.path.exists('scripts'):
    os.makedirs('scripts')

shutil.copyfile('batch-rename.py', 'scripts/batch-rename')

setup(
    name='Batch File Renamer',
    version='1.0.4',
    packages=['batch_renamer_cli'],
    scripts=['scripts/batch-rename'],
    url='https://github.com/darko3/batch-renamer',
    license='MIT',
    author='Girish Oemrawsingh',
    author_email='girish.oemrawsingh@protonmail.com',
    description='An easy to use python script for quickly renaming multiple files ending with incrementing numbers.'
)
