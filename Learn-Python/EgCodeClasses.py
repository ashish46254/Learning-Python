#! /usr/bin/python34

import os
from os import path

import datetime
from datetime import date, time, timedelta

import time

import shutil
from shutil import make_archive

from zipfile import ZipFile


#== Class, Drived Class, Conditionals, functions return, iterator / generator, exception handling
#== OS Path Utils

class mainClass():
    def method1(self):
        x,y = 2,1
        st = "method2" if (x < y) else "method1"
        print ("mainClass  {}".format(st))
    
    def method2(self, someString=""):
        x,y = 1,2
        st = "method2" if (x < y) else "method1"
        print ("mainClass  {}".format(st) + someString)
        return ("executed method2 of mainClass")
    def iterator_fn(self,*args):
        if (len(args) == 1):  start,stop,step=0,args[0],1
        elif (len(args) == 2):  start,stop,step=args[0],args[1],1
        elif (len(args) == 3):  start,stop,step=args[0],args[1],args[2]    
        i = start
        while i <= stop:
            yield i
            i += step 
            
    def error_handler(self):
        try:
            # Exceptlion list at https://docs.python.org/3/library/exceptions.html
            open("ghost.txt")
            #raise FileNotFoundError("file error")
        except FileNotFoundError as e:
            print("error: {} ~~~ {} ~~~ {}".format(e,e.args,e.filename))
#         finally:
#             print("Goodbye")
#             exit()
        
class drivedClass(mainClass):
    def method2(self):
        print ("drivedClass method2")
    
    def method1(self):
        mainClass.method1(self);
        print ("drivedClass method1")
        
    def ospath_utils(self):
        print("OS Path Utils")
        print("Windows" if (os.name == "nt") else os.name)
        print( "Item exists: " + str(path.exists("testfile.txt")))
        print( "Item is a file: " + str(path.isfile("testfile.txt")))
        print( "Item is a directory: " + str(path.isdir("testfile.txt")))
        print( "Item's path: " + str(path.realpath("testfile.txt")))
        pth, fname = path.split(path.realpath("testfile.txt"))
        print( "Item's path and name: " + pth +"  " + fname)
        # modification time
        t = time.ctime(path.getmtime("testfile.txt"))
        print(t)
        print(datetime.datetime.fromtimestamp(path.getmtime("testfile.txt")))
        print("Shell Util - file backup and processed")
        shutil.copy(fname,fname+".bak")
        # copy over the permissions, modification times, and other info
        shutil.copystat(fname,fname+".bak")
        # rename the original file
        os.rename("testfile.txt", "processedfile.txt")
#       
# ZIPping files
    def zip_file(self):
        with ZipFile("testzip.zip","w") as newzip:
            newzip.write("processedfile.txt")
            newzip.write("testfile.txt.bak")
            
    def file_write(self):
        f = open("processedfile.txt","w+")
        # Open the file for appending text
#        f = open("processedfile.txt","a+")
# write some lines of data to the file
        for i in range(10):
            f.write("This is line %d \r" % (i+1))
        f.close()
  
# Open the file back up and read the contents
        f = open("processedfile.txt","r")
        if f.mode == 'r': # check to make sure that the file was opened

# use the read() function to read the entire file
#        contents = f.read()
#        print contents
                fl = f.readlines() # readlines reads the individual lines into a list
                for x in fl:
                    print (x, end="")      
        
def main():
#    c = mainClass()
#     c.method1()
#     c.method2(" Method2 Call")
    c2 = drivedClass()
#     c2.method1()
#     print(c.method2())
#     for i in (c.iterator_fn(25)): print(i,end=" ")
#     print()
#     c.error_handler()
#    c2.ospath_utils()
#    c2.zip_file()
    c2.file_write()  

if __name__ == "__main__":   main()
