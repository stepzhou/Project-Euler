'''
Created on Sep 1, 2011

@author: Admin
'''

from math import sqrt

if __name__ == "__main__":
    p = 0
    a = 1
    b = 1
    primes = [x for x in range(1, 1001)]
    # Dictionary that keeps count of # of times the perimeter value hits.
    perimeters = dict([(x, 0) for x in primes])
    
    while p <= 1000:
        while p <= 1000:
            c = sqrt(a**2 + b**2)
            p = a + b + c
            if p.is_integer():
                # perimeter counter update
                perimeters[p] += 1
            a += 1
        b += 1
        a = b
        c = sqrt(a**2 + b**2)
        p = a + b + c
            
    largest = 0
    pair = ()
    for k, v in perimeters.iteritems():
        if v > largest:
            pair = (k, v)
            largest = v
    
    print pair
        