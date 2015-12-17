# safe_rm

Functionality:
I am writing a script that will move a specified file or directory to a trash folder. I still need to figure out the exact design I want.
Do I want the trash folder to just have all the files floating around with no order? Do I want them to be organized by day? What I was thinking
about before was to just have each file in its own foler, and the folders will be numbered or something so I can undo many times. They will have to be ordered
in some way. Ok I think it makes sense to have all the files floating around in the trash directory, but I will also have an index that contains all the information 
I need to recover the files. You can hit undo as many times as you want. I don't know if anyone would want something like undo -5 that undos the srm you did 5 ties ago. Yeah that seems kind of weird, like how can you even remember that far back. Maybe someone might want do undo something that they did two times ago right?. Also should there be a redo button?

Index:
[full path of the file or directory you deleted. the most recently deleted item will be the last line of the file]

This is how srm will look:
implement a stack somehow. hm maybe just use the linenumbers to keep track of whats what.
#write it to the index

#move it

This is how undo will look:
#remove the most recently deleted item from the index
it will be the last line of the file

#move it back
