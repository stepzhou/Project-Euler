'''
Created on Jul 10, 2011

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.

@author: Admin
'''

"""
5 digit high = 5 * 9**5 = 295245
6 digit high = 6 * 9**5 = 354284
7 digit high = 7 * 9**5 = 413343

7 digit high has less than 7 digits. Limit from 2 to 354284
"""
limit = 354294
power = 5
fifthpowers = []
for x in range(2, limit+1):
    limit = str(x)
    s = 0
    for y in range(len(limit)):
        s += int(limit[y])**power
    if s == x: fifthpowers.append(x)
print sum(fifthpowers)