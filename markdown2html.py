#!/usr/bin/python3
""" check the the requirment"""
from os import path
import sys
if(len(sys.argv) < 2):
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)

markdowni = sys.argv[1]
htmlfile = sys.argv[2]
file_exits = os.path.exists(markdowni)
if not (file_exits):
    print(f"Missing {markdowni}")
    exit(1)
