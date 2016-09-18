#!/usr/bin/python

import os


class Main():
    
    def __init__(self):
        
        self.supported_versions = ['trusty', 'xenial', 'wily', 'vivid']
        
        self.last_version = int(raw_input("New version number: "))
        print
        
        for supported_version in self.supported_versions:
            
            print "Creating directory %s" % supported_version
            os.system("mkdir %s" % supported_version)
            
            print "Creating directory %s/tmp" % supported_version
            os.system("mkdir %s/tmp" % supported_version)
            
            os.system("cp -R br %s" % supported_version)
            os.chdir(supported_version)
            
            self.setup = """
#!/usr/bin/python

import os
from setuptools import setup

setup (
	name = "batch-renamer-cli",
	version = "1.0.2b%s",
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
""" % str(self.last_version)

            
            with open("setup.py", "wb") as f:
                print "Writing setup.py\n"
                f.write(self.setup)
                f.close()
                
            os.system("python setup.py --command-packages=stdeb.command sdist_dsc")
            os.chdir("tmp")
            os.system("dpkg-source -x ../deb_dist/batch-renamer-cli_1.0.2b%s-1.dsc" % str(self.last_version))
            os.chdir("batch-renamer-cli-1.0.2b%s" % str(self.last_version))
            os.system("vim debian/changelog")
            
            # with open("debian/changelog", "wb") as cl:
            #    cl.write(self.changelog)
            #    cl.close()
            
            os.system("debuild -S -sa")
            # print "\n\nUploading %s build to Launchpad.net" % supported_version
            # os.system("dput ppa:darko3/batch-renamer ../batch-renamer-cli_1.0.2b%s-1_source.changes" % self.last_version)
            os.chdir("..")
            os.chdir("..")
            os.chdir("..")
                
            self.last_version += 1
            # print self.last_version
        

if __name__ == "__main__":
    Main()
