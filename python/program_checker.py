#!/usr/bin/python3
# Program to check if command is present on the server or not

import subprocess
import sys

for index,value in enumerate(sys.argv):
    print(index,value)

if len(sys.argv) > 2:
    sys.exit('Script should have only one argument')

command = (sys.argv[1])
process = subprocess.run(['which', command], capture_output=True, text=True)

if process.returncode ==  0:
    print(f'The program "{command}" is installed')
    print(f'Location of bunary is: {process.stdout}')
else:
    print(f'The program "{command}" is not installed')
    print(process.stderr)


