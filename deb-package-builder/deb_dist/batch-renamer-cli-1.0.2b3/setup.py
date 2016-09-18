#!/usr/bin/python

import os
from setuptools import setup

setup (
	name = "batch-renamer-cli",
	version = "1.0.2b3",
	author = "Girish Oemrawsingh",
	author_email = "skrillex2408@gmail.com",
	description = "Batch rename files in a folder quickly.",
	license = "MIT",
	url = "https://github.com/darko3/batch-renamer",
	packages = ['br'],
	entry_points = {
		'console_scripts': ['batch-renamer-cli = br.br:main']
	},
	classifiers = [
		"License :: MIT",
	],
)

