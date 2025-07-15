import sys

class ExtensionError(Exception):
    pass


try:
    FILENAME=sys.argv[1]
except IndexError:
    print("Usage: python3 task1_1.py <filename>")

if "." not in FILENAME:
    raise ExtensionError(f"Provided filename '{FILENAME}' doesn't contain extension.")
else:
    print(f"File extension is .{FILENAME.split(".")[1]}")

