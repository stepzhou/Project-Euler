#!/usr/bin/env python
# date: Apr 22, 2012

import EulerFuncs
import itertools

# laughably brute-force but easy solution
def check_div(n):
    three_dig = 1000
    d8d9d10 = n % three_dig
    if d8d9d10 % 17 != 0:
        return False
    n /= 10
    d7d8d9 = n % three_dig
    if d7d8d9 % 13 != 0:
        return False
    n /= 10
    d6d7d8 = n % three_dig
    if d6d7d8 % 11 != 0:
        return False
    n /= 10
    d5d6d7 = n % three_dig
    if d5d6d7 % 7 != 0:
        return False
    n /= 10
    d4d5d6 = n % three_dig
    if d4d5d6 % 5 != 0:
        return False
    n /= 10
    d3d4d5 = n % three_dig
    if d3d4d5 % 3 != 0:
        return False
    n /= 10
    d2d3d4 = n % three_dig
    if d2d3d4 % 2 != 0:
        return False
    return True

pandigitals = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

s = 0
for x in pandigitals:
    num =  "".join(str(i) for i in x)
    num = int(num)
    # take out permutations that start with '0'
    if num > 1000000000:
        if check_div(num):
            s += num

print s
