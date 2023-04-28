import os
print(os.getcwd())
# os.mkdir("p")  To create directory.This method raises FileExistsError if the directory to be created already exists.
# os.rmdir("p")    To remove folders
# os.remove("p") To remove files
# os.makedirs("l\p") if any intermediate-level directory is missing, os.makedirs() method will create them all.
# os.listdir() return all files and directories 
print(os.name)  #Print system operating system operated module
# os.popen("filename", mode = "w" or "r")
# os.close()  A file opened using open(), can be closed by close()only. But file opened through os.popen(), can be closed with close() or os.close().
# os.rename("oldname","newname")
print(os.path.exists("Bokeh"))      #####   We pass the directory according to the folder open   ######
print(os.path.getsize("Jupyter"))
# print(os.chdir("Bokeh"))
# print(os.getcwd())
# os.walk("filename",topdown = True)  Used to get directory or file names which are in tree format
# path = os.path.join("parent_dir", "child_dir")  used tp join two path
# os.path.isfile(path)  Return true or false 
# os.path.isdir(path)  Return true or false