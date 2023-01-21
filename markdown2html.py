#!/usr/bin/python3
""" check the the requirment"""
from os import path
import sys
if __name__ == "__main__":
    if(len(sys.argv) < 3):
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    elif (not path.exists(sys.argv[0])):
        sys.stderr.write("Missing {}".format(sys.argv[0]))
        sys.exit(1)
    else:
        sys.exit(0)
