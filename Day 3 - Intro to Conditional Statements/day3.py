#!/bin/python3

import sys

N = int(input().strip())

def weirdness(n):
    if n % 2 == 0:
        if n >= 2 and n <= 5:
            return "Not Weird"
        elif n >= 6 and n <= 20:
            return "Weird"
        else:
            return "Not Weird"
    else:
        return "Weird"

print(weirdness(N))