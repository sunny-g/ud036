''' lesson 2 - profanity checker
bulid an app that detects for profanity

steps:
    open a file
    read it's text
    compare each word against those in a profanity array/dict



'''
import sys
import os

def main(argv):
    email_text = open(os.path.realpath(argv[1]))
    profanity_dict = open(os.path.realpath(argv[2]))

    email_contents = email_text.read()
    email_text.close()

    print email_contents

    

if __name__ == '__main__':
    main(sys.argv)
