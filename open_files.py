import os


path = "C:\\Users\\Kevin\\Documents\\TOKEN.txt"


if os.path.exists(path):
    print("The location exits")
    if os.path.isfile(path):
        print("The location exists and is a file")
else:
    print("The location doesn't exists")