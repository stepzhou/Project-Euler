'''
Created on Jul 19, 2011

An irrational decimal fraction is created by concatenating the positive 
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value 
of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

@author: Admin
'''

if __name__ == "__main__":
    # '0.' is superfluous 
    s = ""
    limit = 1
    while len(s) <= 1000000:
        s += str(limit)
        limit += 1
    print (int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999])
           * int(s[99999]) * int(s[999999]))