#!/usr/bin/env python

import math

def match(n):
    n = str(n)
    check = 1
    for i in xrange(0,len(n),2):
        if n[i] != str(check):
            return False
        check += 1
    return True

n = 1020304050607080900
s = str(n)
i = len(s)-2
while i >= 0:
    j = int(s[i]) + 1
    break
    
