#!/usr/bin/python

import os
import shutil
from distutils.core import setup

if not os.path.exists('scripts'):
    os.makedirs('scripts')

shutil.copyfile('batch-rename.py', 'scripts/batch-rename')

setup(
    name='batch-rename',
    version='1.0.4',
    packages=['batch_renamer_cli'],
    scripts=['scripts/batch-rename'],
    url='https://github.com/darko3/batch-renamer',
    download_url='https://github.com/darko3/batch-renamer/archive/1.0.4.tar.gz',
    keywords=['batch-renamer', 'files', 'python'],
    license='MIT',
    author='Girish Oemrawsingh',
    author_email='girish.oemrawsingh@protonmail.com',
    description='An easy to use python script for quickly renaming multiple files ending with incrementing numbers.'
)
