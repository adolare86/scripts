#!/usr/bin/env python3

import os
import shutil

# List all files and Dir
os.listdir()

# print the current directory
print("The current working dir is: ", os.getcwd())

# Create empty directory
dir_name = "/tmp/empty_dir"
os.mkdir(dir_name)

# Delete dir
os.rmdir(dir_name)

# Change the current working dir
os.chdir(dir_name)
print("The current working dir is: ", os.getcwd())

# Create nested dir
nested_dir = "/tmp/nested_dir/dir1"
os.makedirs(nested_dir)

# Delete nested dir
os.removedirs(nested_dir)

# remote non-empty folders
nested_dir1 = "/tmp/nested_dir1"
shutil.rmtree(nested_dir1)

# List all files and Dir
os.listdir()