'''
Created on Jul 21, 2011

Considering quadratics of the form:

limit**2 + an + b, where |a|  1000 and |b|  1000

where |limit| is the modulus/absolute value of limit
e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of check_prime for consecutive values of limit, 
starting with limit = 0.

@author: Admin
'''

def sieveOfErat(end):  
    if end < 2: return []  

    # The array doesn't need to include even numbers  
    lng = ((end/2)-1+end%2)  
    
    # Create array and assume all numbers in array are prime  
    sieve = [True]*(lng+1)  
    
    # In the following code, you're going to see some funky  
    # bit shifting and stuff, this is just transforming n and j  
    # so that they represent the proper elements in the array.  
    # The transforming is not optimal, and the number of  
    # operations involved can be reduced.  
  
    # Only go up to square root of the end  
    for n in range(int(end**0.5) >> 1):  
        # Skip numbers that aren't marked as prime
        if not sieve[n]: continue  

        # Unmark all multiples of n, starting at n**2  
        for j in range( (n*(n + 3) << 1) + 3, lng, (n << 1) + 3):  
            sieve[j] = False  

    # Don't forget 2!  
    check_prime = [2]  

    # Gather all the check_prime into a list, leaving out the composite numbers  
    check_prime.extend([(n << 1) + 3 for n in range(lng) if sieve[n]])  

    return check_prime

def quadratic(limit, a, b):
    return limit**2 + a*limit + b

if __name__ == "__main__":
    check_prime = sieveOfErat(10000)
    # Expedite process by using set
    check = set(check_prime)
    streak, a1, b1, n = 0, 0, 0, 0
    a = -999
    while a < 1000:
        n = 0
        b = check_prime[n]
        while b < 1000:
            limit = 0
            while quadratic(limit, a, b) in check:
                limit += 1
            if limit > streak:
                streak = limit
                a1 = a
                b1 = b
            n += 1
            b = check_prime[n]
        a += 1
    print a1 * b1