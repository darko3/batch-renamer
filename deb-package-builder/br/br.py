#!/usr/bin/python2

"""
MIT License

Copyright (c) 2016 Girish Oemrawsingh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import sys
import time
import getopt

# import the color module I wrote for my projects
from color import Color as tcolor
from color import textType as ttype

version = '1.0.2b'
github_project_page = ttype.bold + tcolor.green + 'https://github.com/darko3/batch-renamer'  + tcolor.white
usage = """
Batch File Renamer %s - (C) 2016 Girish Oemrawsingh
View this project on Github: %s


usage: ./batch-renamer-cli.py [options]

Options:

  -h, --help                        print this help menu and exit
  -p, --folder-path <folder-path>   specify folder path that includes files to rename
  -n, --new-name <new-file-name>    specify the new filename for the files in the folder

""" % (version, github_project_page)


def init(folder, new_name):
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:n:", ["help", "folder-path=", "new-name="])

    except getopt.GetoptError as e:
        print(usage)
        print(str(e) + "\n")
        sys.exit(1)

    for opt, arg in opts:

        if opt in ("-h", "--help"):
            print(usage)
            sys.exit(0)

        elif opt in ("-p", "--folder-path"):
            folder = arg

        elif opt in ("-n", "--new-name"):
            new_name = arg

    if folder == '':
        print(usage)
        sys.exit(1)

    elif new_name == '':
        print(usage)
        sys.exit(1)

    else:
        rename_files(folder, new_name)

def rename_files(folder_path, new_name):
    
    file_counter = 0
    
    print("\nNew name: %s" % new_name)
    print("Folder path: %s\n" % folder_path)
        
    try:
        raw_input(ttype.bold + tcolor.red + """PLEASE CHECK IF THE FOLDER PATH AND NEW NAME IS CORRECT
BECAUSE YOU CAN EASILY RENAME FILES IN ANY FOLDER YOU DID NOT INTEND TO\n
PRESS [ENTER] TO CONTINUE OR CTRL + C TO EXIT\n""" + tcolor.white)

    except NameError:
        input(ttype.bold + tcolor.red + """PLEASE CHECK IF THE FOLDER PATH AND NEW NAME IS CORRECT
BECAUSE YOU CAN EASILY RENAME FILES IN ANY FOLDER YOU DID NOT INTEND TO\n
PRESS [ENTER] TO CONTINUE OR CTRL + C TO EXIT\n""" + tcolor.white)
        
    except KeyboardInterrupt:
        print("\nThank you for using Batch File Renamer by Girish Oemrawsingh.")
        print("You can view this project on Github: %s" % github_project_page)
        sys.exit(2)
        
        
    start = time.time()
    
    for root, dirs, files in os.walk(folder_path):
        
        dirs.sort()
        files.sort()
        
        for f in files:
            file_counter += 1
            file_path = "%s/%s" % (root, f)
            print("Renaming %s" % file_path)
            ext = os.path.splitext(new_name)[1]
            fname = os.path.splitext(new_name)[0]
            os.rename(file_path, "%s/%s %s%s" % (root, fname, file_counter, ext))
            
    end = time.time()
    total_time = end - start
    print("\nFinished renaming %d files with a total time of %f seconds." % (file_counter, total_time))
            

def main():
    folder = ''
    new_name = ''
    init(folder, new_name)
