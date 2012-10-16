import sys

def sumn(n):
    num = 1
    s = 1
    while num < n:
        yield s
        num += 1
        s = num * (3*num - 1) / 2 

for x in sumn(10):
    print x
