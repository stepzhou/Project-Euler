'''
Created on Jun 17, 2011

Find the sum of the digits in the number 100!

@author: Admin
'''

from math import factorial

if __name__ == '__main__':    
    print sum(int(x) for x in str(factorial(100)))