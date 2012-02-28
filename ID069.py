'''
Created on Jan 12, 2012

@author: Admin
'''

import EulerFuncs
import timeit

def ID069():
    limit = 1000001
    totient_vals = _iterate_totient(limit)
    n_over_totient = _divide_n_by_totient(totient_vals)
    return _get_index_of_max_value(n_over_totient)
    
def _iterate_totient(limit):
    """Iteratively calculates the totient function
    for values under a limit
    """
    primes = EulerFuncs.primes_below(limit)
    sieve = [n for n in xrange(limit)]
    
    for p in primes:
        mult = p
        while mult < limit:
            sieve[mult] *= (1-1/float(p))
            mult += p
    return sieve

def _divide_n_by_totient(totient_vals):
    """Iteratively calculates n/phi(n)
    """
    for n, n in enumerate(totient_vals):
        # catch single error for totient_vals[0] = 0
        try:
            totient_vals[n] = n/n
        except ZeroDivisionError:
            pass
    return totient_vals

def _get_index_of_max_value(li):
    return li.index(max(li))

def time_ID069():
    TRIALS = 1
    t = timeit.Timer("ID069()", "from __main__ import ID069")
    print "Avg: %.4f s/pass" % (t.timeit(number=TRIALS)/TRIALS)

if __name__ == "__main__":
    time_ID069()
    
        