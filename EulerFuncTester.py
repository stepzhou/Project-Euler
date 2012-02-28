'''
Created on Jan 8, 2012

@author: Admin
'''

import EulerFuncs
import timeit

def test_sieve_time():
    TRIALS = 20
    t = timeit.Timer("EulerFuncs.primes_below(1000000)", "import EulerFuncs")
    print "Own: %.4f s/pass" % (t.timeit(number=TRIALS)/TRIALS)
    t = timeit.Timer("EulerFuncs.primes_under(1000000)", "import EulerFuncs")
    print "Old: %.4f s/pass" % (t.timeit(number=TRIALS)/TRIALS)
    
def test_pandigital():
    print EulerFuncs.is_pandigital(12345678)
    print EulerFuncs.is_pandigital(123456789)
    print EulerFuncs.is_pandigital(1234567890)
    print EulerFuncs.is_pandigital(203456789)
    print EulerFuncs.is_pandigital(234567189)

if __name__ == "__main__":
    print sum(EulerFuncs.primes_below(1000)[3:24])
    print EulerFuncs.primes_below(1000)[23]