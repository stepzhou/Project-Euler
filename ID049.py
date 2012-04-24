#!/usr/bin/env python
# date: Apr 23, 2012

import EulerFuncs
import itertools

def str_permute(s):
    perms = list(itertools.permutations(s))
    for i in xrange(len(perms)):
        perms[i] = "".join(str(i) for i in perms[i])
    return perms

# find primes 1000 <= primes < 10000
limit = 10000
primes = EulerFuncs.primes_below(limit)
primes = primes[primes.index(1009):]
primes_set = set(primes)

for i in xrange(len(primes)):
    for j in xrange(i+1, len(primes)):
        prime1 = primes[i]
        prime2 = primes[j]
        diff = prime2 - prime1
        prime3 = prime2 + diff
        # check if prime3 is prime
        if prime3 in primes_set:
            prime1_perm = str_permute(str(prime1))
            # check if the three numbers are permutations of one another
            if str(prime2) in prime1_perm and str(prime3) in prime1_perm:
                print prime1, prime2, prime3
