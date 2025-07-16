"""This module counts number of characters in the string."""

import sys

list_of_symbols={}

try:
    arg_string=sys.argv[1]
except IndexError:
    print("Usage: python3 task1_4.py <string>.")


for symbol in arg_string:
    if symbol not in list_of_symbols.keys():
        list_of_symbols[symbol] = 1
    else:
        list_of_symbols[symbol] += 1

out_string=""
for key, value in list_of_symbols.items():
    out_string += f"{key}:{value},"

print(f"{arg_string} -> {out_string[:-1]}")
