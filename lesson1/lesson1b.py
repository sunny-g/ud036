'''////////////////////////
lesson 01 - functions
how would you rename a bunch of files in a folder?

1. open a folder name as input to a function
2. for every appropriate filename, rename the file

//////////////////////////
supplementary notes

many devs just google what they're looking for and learn as they go
many scan documentation just to find what they need

'''

import os
import string

def renameFiles():
    ''' 1. for every file in current folder, rename filename'''
    pwd = os.getcwd() + '/'
    file_list = os.listdir(pwd)

    for filename in file_list:
        filepath = pwd + filename
        os.rename(filepath, pwd + filename.translate(None, "0123456789"))

renameFiles()
