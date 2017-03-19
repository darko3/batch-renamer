#!/usr/bin/python

import os
import shutil
from setuptools import setup

if not os.path.exists('scripts'):
    os.makedirs('scripts')

try:
    shutil.copyfile('batch-rename.py', 'scripts/batch-rename')
except IOError:
    print("Could not copy batch-rename.py file. You can ignore this if you're installing with pip.")

setup(
    name='batch-rename',
    version='1.0.6',
    packages=['batch_renamer_cli'],
    scripts=['scripts/batch-rename'],
    install_requires=['colorama'],
    url='https://github.com/darko3/batch-renamer',
    download_url='https://github.com/darko3/batch-renamer/archive/1.0.6.tar.gz',
    keywords=['batch-renamer', 'files', 'python'],
    license='MIT',
    author='Girish Oemrawsingh',
    author_email='girish.oemrawsingh@protonmail.com',
    description='An easy to use python script for quickly renaming multiple files ending with incrementing numbers.'
)
