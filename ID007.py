'''
Created on Jun 14, 2011

Finds the 10001th prime.

@author: Stephen Zhou
'''

if __name__ == '__main__':
    check_prime = [2,]
    num = 3
    count = 1
    
    while count < 10001:
        isPrime = True
        for x in check_prime:
            if x != 1 and num % x == 0:
                isPrime = False
                break
        if isPrime == True:
            count += 1
            check_prime.append(num)
        num += 2
    print check_prime[-1]