"""This module sorts provided list and print out metadata about it."""

import sys


def get_input():
    user_input = input("Please enter a list of numbers separated by commas (e.g. 1,2,43,2,4):\n")

    if not user_input:
        print("Error: Please provide numbers.")
        sys.exit(1)

    user_list = user_input.split(",")
    print(f"{user_list}")

    try:
        user_list = [int(item) for item in user_list]
    except ValueError as er:
        er_input = str(er).split(': ')[1]
        if type(er_input) == str:
            print(f"\nError: Element {str(er).split(': ')[1]} is not of an integer type.\n")
            sys.exit(1)
    return tuple(user_list)

def print_output(user_list):
    print(f"\nYour tuple is:\n{user_list}")
    uniq_list=tuple(sorted(set(user_list)))
    print(f"\nYour tuple of unique elements:\n{uniq_list}")
    print(f"\nMinimum number: {uniq_list[0]}")
    print(f"Maximum number: {uniq_list[-1]}")

user_list = get_input()
print_output(user_list)