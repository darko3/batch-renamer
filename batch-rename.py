#!/usr/bin/python2

"""
MIT License

Copyright (c) 2017 Girish Oemrawsingh

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

# Import required modules
import os
import sys
import time
import getopt

# This is a 3rd party module, it's needed for colors in the windows commandline
# If you don't have it, you can install it with pip
# $ pip install colorama
import colorama

# import the color module I wrote for my projects
from batch_renamer_cli import Color as TextColor
from batch_renamer_cli import textType as TextType

version = '1.0.3'
github_project_page = TextType.bold + TextColor.green + 'https://github.com/darko3/batch-renamer' + TextColor.white
usage = """
Batch File Renamer %s - (C) 2017 Girish Oemrawsingh
View this project on Github: %s


usage: ./batch-rename.py [options]

Options:

  -h, --help                        print this help menu and exit
  -p, --folder-path <folder-path>   specify folder path that includes files to rename
  -n, --new-name <new-file-name>    specify the new filename for the files in the folder

""" % (version, github_project_page)

rename_warning = """PLEASE CHECK IF THE FOLDER PATH AND NEW NAME IS CORRECT BECAUSE YOU CAN EASILY RENAME FILES IN ANY
FOLDER YOU DID NOT INTEND TO\nPRESS [ENTER] TO CONTINUE OR CTRL + C TO EXIT\n"""


def main(folder, new_name):
    
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
        raw_input(TextType.bold + TextColor.red + rename_warning + TextColor.white)

    except NameError:
        input(TextType.bold + TextColor.red + rename_warning + TextColor.white)
        
    except KeyboardInterrupt:
        print("\n\nThank you for using Batch File Renamer by Girish Oemrawsingh.")
        print("You can view this project on Github: %s\n" % github_project_page)
        sys.exit(1)

    start = time.time()
    
    for root, dirs, files in os.walk(folder_path):
        
        dirs.sort()
        files.sort()
        
        for f in files:
            file_counter += 1
            file_path = "%s/%s" % (root, f)
            print("Renaming %s" % file_path)
            ext = os.path.splitext(new_name)[1]
            file_name = os.path.splitext(new_name)[0]
            os.rename(file_path, "%s/%s-%s%s" % (root, file_name, file_counter, ext))
            
    end = time.time()
    total_time = end - start
    print("Finished renaming %d files with a total time of %f seconds.\n" % (file_counter, total_time))
            

if __name__ == "__main__":
    # folder = ''
    # new_name = ''
    colorama.init()
    main(folder='', new_name='')
