#!/usr/bin/env python
import sys
import os
import argparse
import subprocess as sp
import datetime as dt
import time

#there are two important pieces of information: where the script (or more importantly, the trash folder) is located, and where the file you are deleting is located
#since I am on my system, I know the location of the trash folder. for now I can hard code that in. But for someone else who may want to download my script, I will have to provide a setup script or something that just runs once when they first download so that it will make the trash folder in the location that they want it
#make it so that it works with an optional number of arguments
#I think we don't even need to use the index
def path_to_name(date,path):
    #replace / with _
    return str(date) + path.replace('/','_')

def main(files):
    #first you need to find the location of the script itelf. weird
    me =  os.path.realpath(__file__)
    mydir = os.path.dirname(me) + "/"
    
    #get the date and time
    ts = time.time()
    date = dt.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

    #index = open(mydir+".index",'a')

    for f in files:
        #then you need to find the full file path
        filepath = os.path.realpath(f)
    
        #write the proper information to the index
        #index.write(date + " " + filepath+"\n")
    
        #do the move
        command = "mv " + filepath + " " + mydir + "trash/" + path_to_name(date,filepath)
        sp.call(command.split())

if __name__=="__main__":
    main(sys.argv[1:])


