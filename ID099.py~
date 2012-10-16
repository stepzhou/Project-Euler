#!usr/bin/env python
# date: Apr 23, 2012

import math

file = open("ID099.txt", "r")

largest = 0
ln = 0
i = 1
for line in file:
    line = line.rstrip("\r\n")
    num = line.split(",")
    num = map(int, num)
    log = num[1] * math.log10(num[0])
    if log > largest:
        largest = log
        ln = i
    i += 1

print largest, ln
