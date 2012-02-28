'''
Created on Jul 5, 2011

Starting in the top left corner of a 22 grid, there are 6 routes (without 
backtracking) to the bottom right corner.

@author: Admin
'''

if __name__ == '__main__':
    from math import factorial
    
    # 40 total means 40! 20 same for left 20 same for down means 20!20!.
    print factorial(40)/(factorial(20)**2)