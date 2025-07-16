"""This module contains functionality that print out extension of provided filename"""

import sys

class ExtensionError(Exception):
    """Handles the custom classname ExtensionError."""
    pass


try:
    FILENAME=sys.argv[1]
except IndexError:
    print("Usage: python3 task1_1.py <filename>")

if "." not in FILENAME:
    raise ExtensionError(f"Provided filename '{FILENAME}' doesn't contain extension.")
else:
    print(f"File extension is .{FILENAME.split('.')[1]}")
    