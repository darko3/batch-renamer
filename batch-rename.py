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

# Import a module that can sort alphanumeric strings
from batch_renamer_cli import sort_by_name


version = '1.0.6'
github_project_page = TextType.bold + TextColor.green + 'https://github.com/darko3/batch-renamer' + TextColor.white
usage = """
Batch File Renamer %s - (C) 2017 Girish Oemrawsingh
View this project on Github: %s


usage: ./batch-rename.py --folder-path <folder-path> --new-name <new-file-name> [options]

Required:

  -p, --folder-path <folder-path>   specify folder path that includes files to rename
  -n, --new-name <new-file-name>    specify the new filename for the files in the folder

Options:

  -h, --help                        print this help menu and exit
  -V, --version                     print the Batch Renamer version number and exit
  -v, --verbose                     enable verbose output mode
  -s, --suppress-warnings           don't show warning prompt before renaming files
  -e, --ends-with <string>          specify a string to end file names with (useful for file extensions)
""" % (version, github_project_page)


def main(folder='', new_name='', ends_with=None, suppress_warnings=False, verbose=False):
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hVvsp:n:e:", ["help", "version", "verbose", "suppress-warnings",
                                                                "folder-path=", "new-name=", "ends-with="])

    except getopt.GetoptError as e:
        print(usage)
        print(str(e) + "\n")
        sys.exit(1)

    for opt, arg in opts:

        if opt in ("-h", "--help"):
            print(usage)
            sys.exit(0)

        elif opt in ("-V", "--version"):
            print("Batch File Renamer {}".format(version))
            sys.exit(0)

        elif opt in ("-v", "--verbose"):
            verbose = True

        elif opt in ("-s", "--suppress-warnings"):
            suppress_warnings = True

        elif opt in ("-e", "--ends-with"):
            ends_with = arg

        elif opt in ("-p", "--folder-path"):
            folder = arg

        elif opt in ("-n", "--new-name"):
            new_name = arg

    # Check if folder value is empty
    if folder.isspace() or folder == '':
        print(usage)
        sys.exit(1)

    # Check if new_name value is empty
    if new_name.isspace() or new_name == '':
        print(usage)
        sys.exit(1)

    # Check if ends_with value is not None
    if ends_with:
        # Check if ends_with value is empty
        if ends_with.isspace() or ends_with == '':
            print(usage)
            sys.exit(1)

    # Start rename process if nothing failed
    rename_files(folder, new_name, ends_with=ends_with, verbose=verbose, suppress_warnings=suppress_warnings)


def rename_files(folder_path, new_name, ends_with, verbose, suppress_warnings):

    file_counter = 0
    
    print("\nNew name: {}".format(TextColor.green + new_name + TextColor.white))
    if ends_with:
        print("Ends with: {}".format(TextColor.green + ends_with + TextColor.white))
    print("Folder path: {}\n".format(TextColor.green + folder_path + TextColor.white))

    if verbose:
        print("Verbose mode activated.")
        if not suppress_warnings:
            print("")

    if suppress_warnings:
        if verbose:
            print("Warning prompt will not be shown before renaming.")
            print("")
        else:
            print("Warning prompt will not be shown before renaming.")
            print("")
    else:
        try:
            prompt = ''
            while prompt not in ("y", "yes", "n", "no"):
                try:
                    prompt = raw_input("Are you sure you want to continue with these options? (Y/n): ").lower()
                except NameError:
                    prompt = input("Are you sure you want to continue with these options? (Y/n): ").lower()

                if prompt in ("y", "yes"):
                    print("")
                    pass

                elif prompt in ("n", "no"):
                    print("\nThank you for using Batch File Renamer by Girish Oemrawsingh.")
                    print("You can view this project on Github: %s\n" % github_project_page)
                    sys.exit(0)

        except KeyboardInterrupt:
            print("\nThank you for using Batch File Renamer by Girish Oemrawsingh.")
            print("You can view this project on Github: %s\n" % github_project_page)
            sys.exit(0)

    start = time.time()

    print("Batch renamer started.")

    if verbose:
        print("")

    for root, dirs, files in os.walk(folder_path):
        for f in sort_by_name(files):
            file_counter += 1
            file_path = os.path.join(root, f)

            if verbose:
                print("Renaming %s" % file_path)

            if ends_with:
                os.rename(file_path, "%s/%s-%s%s" % (root, new_name, file_counter, ends_with))
            else:
                os.rename(file_path, "%s/%s-%s" % (root, new_name, file_counter))
            
    end = time.time()
    total_time = end - start

    if verbose:
        print("")

    print("Finished renaming %d files with a total time of %f seconds.\n" % (file_counter, total_time))


if __name__ == "__main__":
    colorama.init()
    main()
