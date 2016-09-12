#!/usr/bin/python

import os
import sys
import time
import pickle
import getopt


class Main():
    
    def __init__(self):
        self.home = os.path.expanduser("~")
        self.folder = ''
        self.file_path = ''
        self.new_name = ''
        self.file_counter = 0
        self.license_agree = ''
        self.usage = """
Batch File Renamer - (C) 2016 Girish Oemrawsingh
View this project on Github: https://github.com/darko3/batch-renamer


usage: ./batch_renamer.py [options]

Options:

  -h, --help\t\t\t\tprint this help menu and exit
  -p, --folder-path <folder-path>\tspecify folder path that includes files to rename
  -n, --new-name <new-file-name>\tspecify the new filename for the files in the folder

            """
        self.license = """
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
        try:
            
            with open("%s/.batch-renamer-cli/agrl.bfr" % self.home, "rb") as handle:
                self.license_agree = pickle.load(handle)
                
        except IOError:

            while self.license_agree != "yes" or "y" or "n" or "no":
                self.license_agree = raw_input("%s\n\nDo you accept the license? \n(Y/n): " % self.license).lower()

                if self.license_agree == "y":
                    self.license_agree = "yes"
                    # print "Agree"
                    with open("%s/.batch-renamer-cli/agrl.bfr" % self.home, "wb") as handle:
                        pickle.dump("yes", handle)
                    break

                elif self.license_agree == "yes":
                    # print "Agree"
                    with open("%s/.batch-renamer-cli/agrl.bfr" % self.home, "wb") as handle:
                        pickle.dump("yes", handle)
                    break

                elif self.license_agree == "n":
                    # print "DisAgree"
                    with open("%s/.batch-renamer-cli/agrl.bfr" % self.home, "wb") as handle:
                        pickle.dump("no", handle)
                    sys.exit(0)

                elif self.license_agree == "no":
                    # print "DisAgree"
                    with open("%s/.batch-renamer-cli/agrl.bfr" % self.home, "wb") as handle:
                        pickle.dump("no", handle)
                    sys.exit(0)
                    
        if self.license_agree == "yes":

            try:
                opts, args = getopt.getopt(sys.argv[1:], "hp:n:", ["help", "folder-path=", "new-name="])

            except getopt.GetoptError as e:
                print self.usage
                print str(e) + "\n"
                sys.exit(0)

            for opt, arg in opts:

                if opt in ("-h", "--help"):
                    print self.usage
                    sys.exit(0)

                elif opt in ("-p", "--folder-path"):
                    self.folder = arg

                elif opt in ("-n", "--new-name"):
                    self.new_name = arg

            if self.folder == '':
                print self.usage
                sys.exit(0)

            elif self.new_name == '':
                print self.usage
                sys.exit(0)

            else:
                # print "Folder Path: %s" % self.folder
                # print "New Name: %s" % self.new_name
                self.rename_files()
                
        else:
            print "You did not agree with the license"
            sys.exit(0)
            
    def rename_files(self):
        
        print "\nNew name: %s" % self.new_name
        print "Folder path: %s\n" % self.folder
        
        try:
            
            enter_to_continue = raw_input("PLEASE CHECK IF THE FOLDER PATH AND NEW NAME IS CORRECT\nBECAUSE YOU CAN EASILY RENAME FILES IN ANY FOLDER YOU DID NOT INTEND TO.\n\nPRESS [ENTER] TO CONTINUE OR CTRL + C TO EXIT\n")
            
        except KeyboardInterrupt:
            print "\nThank you for using Batch File Renamer by Girish Oemrawsingh."
            print "You can view this project on Github: https://github.com/darko3/batch-renamer"
            sys.exit(0)
        
        start = time.time()
        
        for root, dirs, files in os.walk(self.folder):
            
            dirs.sort()
            files.sort()
            
            for file in files:
                self.file_counter += 1
                self.file_path = "%s/%s" % (root, file)
                print "Renaming %s......" % self.file_path
                ext = os.path.splitext(self.new_name)[1]
                fname = os.path.splitext(self.new_name)[0]
                os.rename(self.file_path, "%s/%s %s%s" % (root, fname, self.file_counter, ext))
                
        end = time.time()
        total_time = end - start
        print "Finished renaming %s files with a total time of %s seconds." % (self.file_counter, total_time)
        

def main():
	Main()

        
if __name__ == "__main__":
    
    try:
        home = os.path.expanduser("~")
        os.mkdir("%s/.batch-renamer-cli" % home)
    except OSError as e:
        pass

	main()

