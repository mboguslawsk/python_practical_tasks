"""This module counts number of characters in the string."""

import sys
from collections import Counter

list_of_symbols={}

try:
    arg_string=sys.argv[1]
except IndexError:
    print("Usage: python3 task1_4.py <string>")
    sys.exit(1)

counter = Counter(list(arg_string))

out_string=""
for key, value in counter.items():
    out_string += f"{key}:{value},"

print(f"{arg_string} -> {out_string[:-1]}")
