'''
Created on Jun 13, 2011

Finds the largest palindrome made from the product of two 3-digit numbers.

@author: Admin
'''

def ispalindrome(x):
    z = str(x)
    l = len(z) / 2
    
    if z[:l] == z[-l:][::-1]:
        return 1
    return 0

if __name__ == '__main__':
    n = 999
    j = 999
    
    mults = []
    
    for x in range(1,n+1):
        for y in range(1,j+1):
            mults.append(x * y)
    
    mults.sort()
    
    pally = 0    
    
    for x in mults[::-1]:
        if (ispalindrome(x)):
            pally = x
            break
       
    print pally