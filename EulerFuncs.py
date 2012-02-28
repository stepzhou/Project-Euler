'''
Created on Jun 21, 2011

Sieve of Eratosthenes

@author: Admin
'''
import timeit

def primes_under(end):  
    """
    Returns all check_prime under inputted value.
    """
    
    if end < 2: return []
    lng = ((end/2)-1+end%2)
    sieve = [True]*(lng+1)
    
    for n in range(int(end**0.5) >> 1):  
        if not sieve[n]: continue  
        for j in range( (n*(n + 3) << 1) + 3, lng, (n << 1) + 3):  
            sieve[j] = False  

    check_prime = [2]  

    check_prime.extend([(n << 1) + 3 for n in range(lng) if sieve[n]])  

    return check_prime

def primes_below(limit):
    """
    Returns a list of prime numbers less than n
    limit"""
    if limit < 2: return []
    
    # Marks an index as a prime (True) or non-prime (False)
    sieve = [True] * limit
    p = 3
    # All numbers less than p^2 are marked, terminate if p^2 < limit
    while p ** 2 < limit:
        if sieve[p]:
            n = p ** 2
            # Check start at p^2, multiple of p
            for j in xrange(n, limit, 2 * p):
                sieve[j] = False
        p += 2
        
    check_prime = [2]
    # All non-even Trues after 3 are prime
    for n in xrange(3, len(sieve), 2):
        if sieve[n]: check_prime.append(n)
        
    return check_prime

def is_pandigital(limit):
    """
    Returns whether a number is 1-9 pandigital
    """
    ndigs = 9 
    limit = str(limit)
    primes = []
    for d in limit:
        if d == '0': return False
        primes.append(d)
    return len(primes) == ndigs and len(set(primes)) == ndigs

def check_prime(limit):
    '''check if integer limit is a prime'''
    # range starts with 2 and only needs to go up the squareroot of limit
    for x in range(2, int(limit**0.5)+1):
        if limit % x == 0:
            return False
    return True

