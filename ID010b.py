'''
Created on Jun 14, 2011

Finds the sum of all the primes below two million using sieve of
Eratosthenes.

INCOMPLETE

@author: Admin
'''

if __name__ == '__main__':
    limit = 2000000
    
    nums = range(2, limit)
    
    n = 0
    p = 0
    
    while n < len(nums):
        p = nums[n]
        marked = []
        for x in nums[n+1:]:
            if x % p == 0:
                marked.append(x)
                print x
        
        for x in marked:
            nums.remove(x)
            
        n += 1
        
    sum = 0
        
    for x in nums:
        sum += x
    
    print sum