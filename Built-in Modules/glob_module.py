import glob

# print(glob.glob("*.py"))  # * used to print all files
# print(glob.glob("p*.py"))  used to print file started with p

# print(glob.glob("[0-9]*.py"))   #used to print file started with number(0-9)
# print (glob.glob("[0-9]?.py"))  #used to print file started with number(0-9) with any single digit, ?-represents single digit
# print(glob.glob("*"))    print all files and folders

# recursive(**) - check all the sub-folders also
print(glob.glob("*.py"))
print(glob.glob("**/*.py",recursive= True))