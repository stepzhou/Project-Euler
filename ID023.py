'''
Created on Jul 7, 2011

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.

Solution found online. Comments by me.

@author: Admin
'''

from math import sqrt
 
def d(limit):
    """
    Returns the sum of proper divisors of limit
    """
    # sum
    s = 1
    t = sqrt(limit)
    for n in range(2, int(t)+1):
        if limit % n == 0: s += n + limit / n
    if t == int(t): s -= t
    return s

# Every number above limit is a sum of two abundant #s
limit = 20162
s = 0
abn = set()
for limit in range(1, limit):
    if d(limit) > limit:
        abn.add(limit)
    if not any( (limit-a in abn) for a in abn ):
        s += limit
    
print "Answer to PE23 = ", s