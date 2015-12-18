#!/usr/bin/env python
import sys
import os
import argparse
import subprocess as sp

def path_to_name(date,path):
    #replace / with _
    return str(date) + path.replace('/','_')

def main():
    #first you need to find the location of the script itelf. weird
    me =  os.path.realpath(__file__)
    mydir = os.path.dirname(me) + "/"
    index = open(mydir+".index",'r')
    
    #figure out what you are moving back by reading the .index file
    lines = index.readlines()
    last = lines[len(lines)-1]
    date,filepath = last.split()
    index.close()
    index = open(mydir+".index",'w')

    #delete it from the .index file
    for i in range(0,len(lines)-1):
        index.write(lines[i])
    index.close()

    #get the local part of the file name
    #dirs = filepath.split("/")
    #local = dirs[len(dirs) - 1]

    fname = path_to_name(date,filepath)

    #move it back
    command = "mv "+ mydir+"/trash/" + fname + " " + filepath
    sp.call(command.split())

if __name__=="__main__":
    main()
