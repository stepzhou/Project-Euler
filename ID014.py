'''
Created on Jun 17, 2011

The following iterative sequence is defined for the set of positive integers:

limit  limit/2 (limit is even)
limit  3n + 1 (limit is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

@author: Admin
'''

def collatzconjecture(num):
    """
    Returns the number of iterations it takes for a number to finish the 
    sequence.
    """
    count = 1
    
    while num > 1:
        if (num % 2 == 0):
            num /= 2
        else:
            num = 3 * num + 1
        
        count += 1
    
    return count
    
if __name__ == '__main__':
    biggest = 0
    limit = 0
    limit = 1000000
    
    for x in xrange(1, limit):
        num = collatzconjecture(x)
        # print "start: %6d biggest: %d" % (x, biggest)
        if (num > biggest):
            biggest = num
            limit = x
    
    print "start: %6d biggest: %d" % (limit, biggest)