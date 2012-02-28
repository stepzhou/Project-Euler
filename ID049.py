'''
Created on Jan 26, 2012

@author: Admin
'''

import EulerFuncs

if __name__ == "__main__":
    limit = 10000
    primes = EulerFuncs.primes_below(limit)
    primes = primes[primes.index(1009):]
    
    print primes