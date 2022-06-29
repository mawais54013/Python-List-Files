# script that shows the output of all of the files in a directory:

# method 1:
import os

def file_path(pathInput):
    dir_list = os.listdir(pathInput)
    return "Files and directories in ", pathInput, ": ", dir_list

# example path
print(file_path("/Users/<user_name>/Desktop"))

# method 2:
def file_path2(pathInput2):
    for (root, dirs, file) in os.walk(pathInput2):
        for f in file:
            print(f)

print(file_path2("/Users/<user_name>/Desktop"))