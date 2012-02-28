'''
Created on Sep 2, 2011

@author: Admin
'''

from itertools import permutations
from EulerFuncs import primesunder
from EulerFuncs import isprime

def tuple_to_str(tup):
    """
    Function to facilitate usage of the permutations method.
    Returns the tuple as one string.
    """
    s = ""
    for n in tup:
        s += str(n)
    return s

if __name__ == "__main__":
    limit = 9
    large = 0
    s = ""
    # Maximum 1 - 9 (987654321 is the max)
    # Probably could make seach faster by looking backwards.
    for k in range(1, limit+1):
        s += str(k)
        for v in permutations(s, len(s)):
            x = tuple_to_str(v)
            print x
            if isprime(int(x)) and int(x) > large:
                large = int(x)
    # SO FUCKING SLOOW
    print "large: ", large
            
            