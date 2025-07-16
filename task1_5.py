"""This module show statistics about physical machine."""

import sys, platform, os
import psutil, requests


def print_usage():
    """This function shows usage of this module."""
    print("Usage: python3 task1_4.py [-d] [-m] [-c] [-u] [-l] [-i].")
    print('''   -d for distribution information,
                -m for memory information, 
                -c for CPU information, 
                -u for user information, 
                -l for load average information, 
                -i for IP address''')


file_args=sys.argv[1:]

for argum in file_args:
    if argum == "-d":
        print(f"Distribution information:\t\t{platform.system()}, {platform.version()}")

    elif argum == "-m":
        mem=psutil.virtual_memory()
        mem_total = mem.total / 1073741824
        mem_used = round( mem.used / 1073741824, 2 )
        mem_free = round( mem.free / 1073741824, 2 )
        print(f"Memory information:\t\tTotal {mem_total} GB" \
              f", Used {mem_used} GB, Free {mem_free} GB")

    elif argum == "-c":
        model_proc=platform.processor()
        cores = psutil.cpu_count(logical=False)
        freq_current = psutil.cpu_freq().current
        freq_min = psutil.cpu_freq().min
        freq_max = psutil.cpu_freq().max
        print(f"CPU information:\t\tModel {model_proc}, Cores number {cores}"
              f", Current frequency {freq_current} MHz,")
        print(f"\t\t\t\t Minimum frequency {freq_min} MHz, Maximum Freuency {freq_max}")

    elif argum == "-u":
        print(f"Current user is:\t\t{os.getlogin()}")

    elif argum == "-l":
        la1, la5, la15 = os.getloadavg()
        print(f"Load average information:\t1 min {la1}, 5 min {la5}, 15 min {la15}")

    elif argum == "-i":
        public_ip = requests.get('https://api.ipify.org', timeout=5).text
        print(f"Public IP is:\t\t\t{public_ip}")
