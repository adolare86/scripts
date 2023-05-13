#!/usr/bin/env pyton3

# Import the OS Module
import os

name_of_dir = "/tmp/example"

try:
    # Create the new directory
    os.mkdir(name_of_dir)
    print(f"Directory {name_of_dir} created successfully")

# Print the result, in case directory already exists
except FileExistsError:
    print(f"Directory {name_of_dir} already exist")


