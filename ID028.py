'''
Created on Jul 10, 2011

Starting with the number 1 and moving to the right in a clockwise direction a 
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
 in the same way?

@author: Admin
'''

# top right diag, top left diag.....
tr, tl, bl, br = 0, 0, 0, 0
side = 1001
# doesn't include 1
for x in range(3, side+1, 2):
    tr += x**2
    tl += x**2 - x + 1
    bl += x**2 - 2*x + 2
    br += x**2 - 3*x + 3

print tr + tl + bl + br + 1