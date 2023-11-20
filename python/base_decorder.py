#!/usr/bin/python3

import argparse
import base64
import sys

"""
 usage - use to share syntax of script
 epilog - use to print last message of help. We can give the example
"""
parser = argparse.ArgumentParser(description="Python script to decode base64 and base32"
                                 ,usage="%(prog)s --b64/--b32 cypher"
                                 ,epilog="Example %(prog)s --b64 aGVsbG8=" )
"""
dest - Value of argument stores in this variable
metavar - Full form of argument
nargs - Number of argument
required - True if argument is compulsory
choices - Static list of argument values
"""                       
parser.add_argument("--b64"
                    ,help="Decode Base64 cypher"
                    ,dest="b64"
                    ,metavar="base64",
                    nargs="+")

parser.add_argument("--b32"
                    ,help="Decode Base32 cypher"
                    ,dest="b32"
                    ,metavar="base32",
                    nargs="+")

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()

b64 = args.b64
b32 = args.b32

if b64:
    for cypher in b64:
        print(base64.b64decode(cypher).decode())

if b32:
    for cypher in b32:
        print(base64.b32decode(cypher).decode())