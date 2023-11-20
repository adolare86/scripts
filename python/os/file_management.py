#!/usr/bin/env pyton3

import os

# Create a file
test_file = "/tmp/text.txt"
text_file = open(test_file, "w")
text_file.write("Test file")

# Rename file
os.rename(test_file, "/tmp/text2.txt")

#  Move file to other dir
os.replace("/tmp/text2.txt", "/tmp/text3,txt")

# List all files and Dir
os.listdir("/tmp")


os.