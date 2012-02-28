'''
Created on Jan 2, 2012

@author: Admin
'''

from math import *

def num_comb(limit, r):
    d = factorial(limit)
    limit = factorial(r) * factorial(limit-r)
    return d/limit

if __name__ == "__main__":
    N_MIN = 23
    R_MIN = 10
    THRESHOLD = 1000000
    
    limit = N_MIN
    r = R_MIN
    c = 0
    
    while limit <= 100:
        while r <= limit:
            if num_comb(limit,r) > THRESHOLD:
                c += 1
            r += 1
        r = 1
        limit += 1
    
    print c