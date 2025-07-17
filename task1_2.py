"""This module sorts provided list and print out metadata about it."""

import sys


def get_input():
    user_input = input("Please enter a list of numbers separated by commas (e.g., 1, 2, 43, 12, 4):\n")

    user_list = user_input.split(",")

    try:
        user_list = [int(item) for item in user_list]
    except ValueError as er:
        er_input = str(er).split(': ')[1]
        if er_input == "\'\'":
            print("Error: Please provide numbers.")
            sys.exit(1)
        else:
            print(f"\nError: Element {str(er).split(': ')[1]} is not of integer type.\n")
            sys.exit(1)
    return user_list

def print_output(user_list):
    print(f"\nYour list is:\n'{user_list}'")
    uniq_list=list(set(user_list))
    print(f"\nYour list of unique elements:\n'{uniq_list}'")
    sorted_unique = sorted(uniq_list)
    print(f"\nSorted unique list is \n'{sorted_unique}'")
    print(f"\nMinimum number: {sorted_unique[0]}")
    print(f"Maximum number: {sorted_unique[-1]}")

user_list = get_input()
print_output(user_list)