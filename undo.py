#!/usr/bin/env python
import sys
import os
import argparse
import subprocess as sp
import glob

def path_to_name(date,path):
    #replace / with _
    return str(date) + path.replace('/','_')

def oldmain():
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

def latest(files,trashdir):
    lastfile = files[len(files)-1]
    date = lastfile.split('_')[0]

    command = "ls " + trashdir + date + "*"
    pattern = trashdir + date + "*"
    print command
    
    #latest_files = sp.check_output(command.split()).split()
    latest_files = glob.glob(pattern)
    return latest_files

def move(f,trashdir):
    #first turn filename in trash to the location you want to move it
    print "f in move: " + f
    parts = f.split('/')
    last = parts[len(parts) - 1]
    name = last.replace('_','/')
    print "name: " + name
    namelist = name.split('/')[1:]
    print "namelist: " + str(namelist)
    fname = "/" + '/'.join(namelist)

    print "fname: " + fname

    #then do the move
    command = "mv " + f + " " + fname
    print "command: " + command
    sp.call(command.split())

def main():
    #first you need to find the location of the script itelf. weird
    me =  os.path.realpath(__file__)
    mydir = os.path.dirname(me) + "/"
    trashdir = mydir + "trash/"
    
    #figure out which files you are moving back by getting the list of files with the most recent date
    command = "ls " + trashdir
    files = sp.check_output(command.split()).split()
    movefiles = latest(files,trashdir)

    for f in movefiles:
        move(f,trashdir)


if __name__=="__main__":
    main()
