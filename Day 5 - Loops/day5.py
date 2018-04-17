#!/bin/python3

import sys


n = int(input().strip())

for i in range(1,11):
    result = i * n
    print("%d x %d = %d" % (n,i,result))

