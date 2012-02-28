'''
Created on Jun 11, 2011

@author: Admin
'''

from math import sqrt

def largestPrimeFactor(number):
    check_prime = [2,]
    num = 3
    
    while num < sqrt(number):
        isPrime = True
        for x in check_prime:
            if x != 1 and num % x == 0:
                isPrime = False
                break
        if isPrime == True:
            check_prime.append(num)
        num += 2
        print str(num) + " " + str(sqrt(number))
    
    current = 0
    
    for x in check_prime:
        if (number % x == 0):
            current = x
    
    return current
        
if __name__ == '__main__':
    print largestPrimeFactor(600851475143)