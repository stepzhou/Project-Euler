'''
Created on Jul 7, 2011

@author: Admin
'''

from itertools import permutations

if __name__ == "__main__":
    for idx, x in enumerate(permutations("0123456789", 10)):
        if idx+1 == 1000000:
            print x
            break