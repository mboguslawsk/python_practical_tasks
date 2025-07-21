"""This module contains functionality that print out extension of provided filename"""

import sys, os

class ExtensionError(Exception):
    """Handles the custom classname ExtensionError."""
    pass



number_of_args = (len(sys.argv)-1)
if number_of_args != 1:
    print("\nError: Provide one argument.")
    print("Usage: python3 task1_1.py <filename>\n")
    sys.exit(1)
else:
    filename=sys.argv[1]


_, extension = os.path.splitext(filename)

if extension == "":
    raise ExtensionError(f"Provided filename '{filename}' doesn't contain extension.")
else:
    print(f"File extension is {extension}")

