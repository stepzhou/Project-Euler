'''
Created on Jan 2, 2012

@author: Admin
'''
'''
Created on Jul 10, 2011

@author: Admin
'''

from math import factorial

"""
9! * 7 is seven digits. 9! * 8 is 7 digits. Therefore,
the largest possible sum will be 9! * 7 = 2540160.
"""
limit = 2540160
factsum = []
for x in range(3, limit+1):
    limit = str(x)
    s = 0
    for y in range(len(limit)):
        s += factorial(int(limit[y]))
    if s == x: factsum.append(x)
    
print sum(factsum)