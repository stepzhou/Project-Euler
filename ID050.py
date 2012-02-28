'''
Created on Jan 3, 2012

@author: Admin
'''

import EulerFuncs
import timeit

def ID050():
    limit = 1000000
    primes = EulerFuncs.primes_below(limit)
    check_prime = set(primes)
    
    p_sums = [0]
    s = 0
    # Sum of consecutive primes
    for p in primes:
        s += p
        if s >= limit: break
        p_sums.append(s)
    
    longest = 0
    prime = 0
    # Checks sum of all combinations of primes that sums < limit
    for n, p_sum_small in enumerate(p_sums):
        for j, p_sum_big in enumerate(p_sums):
            num_btw = j-n
            difference = p_sum_big - p_sum_small
            # 'in' for a set is much faster than with a list
            if num_btw > longest and difference in check_prime:
                longest = num_btw
                prime = difference
    return "num consecutive: %s, prime: %s" % (longest, prime)

def test_ID050_time():
    TRIALS = 10
    t = timeit.Timer("ID050()", "from __main__ import ID050")
    print "Avg: %.4f s/pass" % (t.timeit(number=TRIALS)/TRIALS)
    
if __name__ == "__main__":
    print ID050()
    test_ID050_time()
    