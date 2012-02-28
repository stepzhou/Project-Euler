'''
Created on Jan 26, 2012

@author: Admin
'''

import timeit

def ID112():
    count = 0
    n = 1
    prop = 0.0
    
    while prop != 0.99:
        n += 1
        if is_bouncy(n):
            count += 1
            prop = float(count) / n
    print n

def is_bouncy(n):
    s = str(n)
    inc, dec = False, False
    for i in xrange(len(s)-1):
        if s[i+1] > s[i]:
            inc = True
        if s[i+1] < s[i]:
            dec = True
        if inc and dec:
            return True
    return False

def time_ID112():
    TRIALS = 1
    t = timeit.Timer("ID112()", "from __main__ import ID112")
    print "Avg: %.4f s/pass" % (t.timeit(number=TRIALS)/TRIALS)

def test_funcs():
    print is_bouncy(155349) # True
    print is_bouncy(134468) # False
    print is_bouncy(66420) # False

if __name__ == "__main__":
    time_ID112()
    #test_funcs()