"""This module sorts provided list and print out metadata about it."""

import sys

user_input = input("Please enter a list of numbers separated by commas (e.g., 1, 2, 43, 12, 4):\n")

user_list = user_input.split(",")

try:
    user_list = [int(item) for item in user_list]
except ValueError as er:
    print(f"\nError: Element {str(er).split(': ')[1]} is not of integer type.\n")
    sys.exit(1)



print(f"\nYour list is:\n'{user_list}'")
uniq_list=list(set(user_list))
print(f"\nYour list of unique elements:\n'{uniq_list}'")

print(f"\nSorted unique list is \n'{sorted(uniq_list)}'")

print(f"\nMinimum number: {sorted(uniq_list)[0]}")

print(f"Maximum number: {sorted(uniq_list)[-1]}")
