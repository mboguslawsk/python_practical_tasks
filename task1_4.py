"""This module counts number of characters in the string."""

import sys
from collections import Counter

try:
    arg_string=sys.argv[1]
except IndexError:
    print("\nProvide a string as an argument.")
    print("Usage: python3 task1_4.py <string>\n")
    sys.exit(1)

counter = Counter(arg_string)

out_string=""
for key, value in counter.items():
    out_string += f"{key}:{value},"

print(f"{arg_string} -> {out_string[:-1]}")
