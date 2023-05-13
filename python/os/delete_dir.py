#!/usr/bin/env pyton3

# Import the OS Module
import os

name_of_dir = "/tmp/example"

try:
    # Create the new directory
    os.rmdir(name_of_dir)
    print(f"Directory {name_of_dir} deleted successfully")

# Print the result, in case directory not  exists
except FileNotFoundError:
   print(f"Directory {name_of_dir} doesn't exist")


