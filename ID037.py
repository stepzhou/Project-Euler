'''
Created on Sep 1, 2011

@author: Admin
'''

from EulerFuncs import *

if __name__ == "__main__":
    # Arbitrary high limit
    limit = 1000000
    check_prime = primesunder(limit)
    primes_check = set(check_prime)
    
    truncatables = []
    num_trunc = 0
    n = 4
    while num_trunc < 11:
        p = str(check_prime[n])
        LR, RL = p, p
        # Number of check_prime in series
        # 1 is the starting prime
        LR_n, RL_n = 1, 1
        while len(LR) > 1:
            # Truncate LR
            LR = LR[1:]
            if int(LR) in primes_check:
                LR_n += 1
            # Truncate RL
            RL = RL[:-1]
            if int(RL) in primes_check:
                RL_n += 1
        
        if LR_n == len(p) and RL_n == len(p):
            num_trunc += 1
            truncatables.append(int(p))
            print truncatables
        
        n += 1
    
    print sum(truncatables)
            
        