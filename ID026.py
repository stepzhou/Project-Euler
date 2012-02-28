'''
Created on Jul 29, 2011

@author: Admin
'''

from EulerFuncs import *


def repeated(s):
    """
    Returns true if the number has repeated.
    """
    # Only even numbers should be checked.
    if len(s) < 2 or len(s) % 2 != 0:
        return False
    idx1 = 0
    idx2 = len(s)/2
    for n in range(len(s)/2):
        if s[idx1] != s[idx2]:
            return False
        idx1 +=1
        idx2+=1
    return True      

if __name__ == "__main__":
    # 2, 3, and 5 screw up algorithm
    check_prime = set(primesunder(1000)[3:])
    longest = 0
    limit = 0
    for p in check_prime:
        # Basically just hand-division algorithm
        rem = 1
        div = p
        s = ""
        while rem < div:
            rem *= 10
        while not repeated(s):
            s += str(rem/div)
            rem = rem % div * 10
        if len(s)/2 > longest:
            longest = len(s)/2
            limit = div
        print limit, longest