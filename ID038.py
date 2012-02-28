'''
Created on Jan 3, 2012

@author: Admin
'''

import EulerFuncs
import timeit

def ID038():
    n = 9182
    stop = 10000
    limit = 1000000000
    largest = 918273645
    for n in xrange(n, stop):
        product_concat = str(n)
        n = 2
        while 1:
            product = n*n
            n += 1
            if int(product_concat + str(product)) > limit: break
            product_concat += str(product)
        if int(product_concat) > largest and EulerFuncs.is_pandigital(product_concat):
            largest = int(product_concat)
    return largest

def test_ID038_time():
    TRIALS = 10
    t = timeit.Timer('ID038', 'from __main__ import ID038')
    print "Avg: %.10f s/pass" % (t.timeit(number=TRIALS)/TRIALS)

if __name__ == "__main__":
    print ID038()
    test_ID038_time()