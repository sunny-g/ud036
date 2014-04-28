''' lesson 2 - profanity checker
bulid an app that detects for profanity

steps:
    open a file
    read it's text
    compare each word against those in a profanity array/dict

open()
    returns an object of type file
    open() also calls an init func

urlopen()
    opens a network object to a site
    read() then reads the object

what is an object?
    brad is obj/instance of class Turtle
    email_text is an obj of class File

CONNECTING IDEAS IN LESSON 2
    brad = turtle.Turtle()
        creates an obj of type Turtle which can go forward()
    quotes = open(file)
        creates an obj of type File which can be read()
    cxn = urllib.urlopen()
        creates a File-like obj which can be read()

'''
import sys
import os
import urllib

def main(argv):
    email = open(os.path.realpath(argv[1]))
    email_contents = email.read()
    # print email_contents
    email.close()

    check_profanity(email_contents)


def check_profanity(text):
    dict = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text)
    response = dict.read()
    # print(response)
    dict.close()

    if 'true' in response:
        print('PROFANITY ALERT!')
    elif 'false' in response:
        print('The text is clean of profanity.')
    else:
        print('The input text could not be analyzed.')


# instead of just calling main, we write this
# this prevents main from being run when just importing the module
if __name__ == '__main__':
    main(sys.argv)
