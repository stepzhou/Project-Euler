'''
Created on Jul 7, 2011

Let d(limit) be defined as the sum of proper divisors of limit (numbers less than limit 
which divide evenly into limit).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 
55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

@author: Admin
'''

def divisorGenerator(limit):
    """
    Generates a numbers proper divisors (excluding itself)
    """
    for n in xrange(1,limit/2+1):
        if limit%n == 0: yield n
    
if __name__ == "__main__":
    # Sum of amicable pairs
    pairsum = 0
    for limit in xrange(1, 10001):
        # Sum of limit's proper divisors
        asum = 0
        # Sum of asum's proper divisors
        bsum = 0
        for x in divisorGenerator(limit):
            asum += x
        for y in divisorGenerator(asum):
            bsum += y
        # print "limit: %s asum: %s bsum: %s" % (limit, asum, bsum)
        if limit == bsum and limit != asum: pairsum += limit
    
    print pairsum