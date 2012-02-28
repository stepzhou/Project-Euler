'''
Created on Jun 14, 2011

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

@author: Admin
'''

from math import sqrt

def findabc(sum):
    """
    a + b + c = sum. Takes a sum and returns the Pythagorean triplet whose
    sum equals the inputted sum.
    """
    for a in xrange(1, sum):
        for b in xrange(1, sum):
            c = sqrt(a**2 + b**2)
            # Testing
            print "a: %s b: %s c: %s" % (a, b, c)
            # Breaks if the current sum is greater than the inputted sum
            if (a + b + c > sum):
                break
            # Value found
            if (a + b + c == sum):
                return (a, b, c)

if __name__ == '__main__':
    mult = 1
    
    for x in findabc(1000):
        mult *= x
    
    # Casting to get rid of unnecessary decimal
    mult = int(mult)
    
    print mult