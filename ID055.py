'''
Created on Jan 3, 2012

@author: Admin
'''

def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

def reverse_int(limit):
    limit = str(limit)
    return int(limit[::-1])

def is_lychrel(limit, l=50):
    s = limit + reverse_int(limit)
    print s
    for x in xrange(l):
        if is_palindrome(s):
            return False
        s = s + reverse_int(s)
    return True

if __name__ == "__main__":
    limit = 10000
    c = 0
    for n in xrange(limit):
        if is_lychrel(n):
            c+=1
    print c
