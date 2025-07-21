"""This module counts number of agents and number of requests they made."""

import sys, os, re
from collections import defaultdict
from pprint import pprint

list_of_agents=defaultdict(lambda: defaultdict(int))

try:
    filename=sys.argv[1]
except IndexError:
    print("\nUsage: python3 task1_3.py <filename>.")
    print("Tip: You can use the 'access.log.5' file as an example; " \
                "it is included in the provided materials\n")
    sys.exit(1)

if not os.path.exists(filename):
    print(f"File '{filename}' does not exists.")
    sys.exit(1)

with open(filename, "r") as file:
    for line in file:
        curr_agent = line.split("\"")[-2]
        pattern = r'"(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s+'
        request_cmd = re.search(pattern, line)
        if not (request_cmd is None):
            request_cmd = request_cmd.group(1)

        if request_cmd:
            list_of_agents[curr_agent][request_cmd] += 1


print(f"\nTotal number of unique agents is: {len(list_of_agents.keys())}\n\n")

agent_labels = [f"Agent {key}" for key in list_of_agents]
max_len = max(len(label) for label in agent_labels)


for key, value in list_of_agents.items():
    agent_string=f"Agent {key}"
    output_string= f"{agent_string:<{max_len}}"
    if not value:
        output_string = output_string + f"\t0"
    else:
        for request, num in value.items():
            output_string = output_string + f"\t{request}\t{num} times;"
    print(output_string)
