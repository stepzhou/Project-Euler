'''
Created on Jun 14, 2011

Finds the sum of all the check_prime below two million using brute force.

@author: Admin
'''

from math import sqrt

if __name__ == '__main__':
    check_prime = [2, 3]
    num = 5
    count = 1
    
    while (num < 2000000):
        isprime = True
        limit = int(sqrt(num)) + 1
        
        for x in range(3, limit, 2):
            if (num % x == 0):
                isprime = False
        
        if isprime:
            check_prime.append(num)
        
        num += 2
        
        print num
    
    sum = 0
    
    for x in check_prime:
        sum += x
        
    print sum