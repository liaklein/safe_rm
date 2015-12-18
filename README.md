# safe_rm

Functionality:
I am writing a script that will move a specified file or directory to a trash folder. I still need to figure out the exact design I want.
Current Design: Make a new directory, call it whatever you want (safe makes sense). Download the two scripts into this directory.
Run the 'initialize' script. This script will make a subdirectory called trash and a file called .index.
After you run initialize you can run safe_rm and undo.
I suggest you make aliases to these to scripts for ease of use
As of now, you can only safe_rm local file names, not full path names.
Also, you cannot safe rm two different files with the same name.
These are both issues that I am going to fix.


Index:
[full path of the file or directory you deleted. the most recently deleted item will be the last line of the file]

