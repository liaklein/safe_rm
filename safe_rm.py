#!/usr/bin/env python
import sys
import os
import argparse
import subprocess as sp

#there are two important pieces of information: where the script (or more importantly, the trash folder) is located, and where the file you are deleting is located
#since I am on my system, I know the location of the trash folder. for now I can hard code that in. But for someone else who may want to download my script, I will have to provide a setup script or something that just runs once when they first download so that it will make the trash folder in the location that they want it
def main(local):
    #first you need to find the location of the script itelf. weird
    me =  os.path.realpath(__file__)
    mydir = os.path.dirname(me) + "/"
    #then you need to find the current working directory
    filepath = os.path.realpath(local)
    #write the proper information to the index
    index = open(mydir+".index",'a')
    index.write(filepath+"\n")
    #do the move
    #bug if there is a name clash.
    command = "mv " + local + " " + mydir + "trash/"
    sp.call(command.split())

if __name__=="__main__":
    main(sys.argv[1])


