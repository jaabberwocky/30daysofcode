#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# reverse array, then call print function with " " instead of \n as default end
for num in reversed(arr):
    print(num, end=" ")