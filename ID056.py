'''
Created on Jan 3, 2012

@author: Admin
'''

def sum_digits(limit):
    limit = str(limit)
    s = 0
    for digit in limit:
        s += int(digit)
    return s

if __name__ == "__main__":
    largest = 0
    for a in xrange(1,100):
        for b in xrange(1,100):
            summed = sum_digits(a**b)
            if summed > largest:
                largest = summed
            print a,b
    print largest