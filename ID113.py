'''
Created on Jan 26, 2012

@author: Admin
'''

def ID113():
    lim = 345
    count = 0
    for x in range(1,1000):
        if not is_bouncy(x):
            print x
            
    print count

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

if __name__ == "__main__":
    ID113()