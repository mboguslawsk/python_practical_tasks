import sys, os, re
from pprint import pprint

list_of_agents={}

try:
    filename=sys.argv[1]
except IndexError:
    print("Usage: python3 task1_3.py <filename>.")
    print("Tip: You can use the 'access.log.5' file as an example; it is included in the provided materials")

if not os.path.exists(filename):
    print(f"File '{filename}' does not exists.")
    sys.exit(1)

with open(filename, "r") as file:
    for line in file:
        curr_agent = line.split(" -")[0]
        request_cmd = re.search(r'"\w+ /', line)
        if not request_cmd == None:
            request_cmd = re.search(r'\w+', request_cmd.group()).group()

        if request_cmd:
            if curr_agent not in list_of_agents.keys():
                list_of_agents[curr_agent]= { request_cmd : 1 }
            else:
                if request_cmd not in list_of_agents[curr_agent].keys():
                    list_of_agents[curr_agent][request_cmd ]= 1
                else:
                    list_of_agents[curr_agent][request_cmd] += 1
        else:
            list_of_agents[curr_agent]= {}

        
print(f"\nTotal number of unique agents is: {len(list_of_agents.keys())}\n\n")

for key, value in list_of_agents.items():
    output_string=f"Agent {key}"
    if not value:
        output_string = output_string + f"\t0"
    else:
        for request, num in value.items():
            output_string = output_string + f"\t{request}\t{num} times;"
    print(output_string)