import os
import subprocess as sp

print "This script will initialize a trash folder then self destruct"

command = "mkdir trash"
sp.call(command.split())
command = "touch trash/.index"
sp.call(command.split())

#os.remove(__file__)




