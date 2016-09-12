#!/usr/bin/python

import os
from setuptools import setup
from nvpy import nvpy

setup (
	name = "batch-renamer-cli",
	version = "1.0.1",
	author = "Girish Oemrawsingh",
	author_email = "skrillex2408@gmail.com",
	description = "Rename files in a folder fast!",
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
	

