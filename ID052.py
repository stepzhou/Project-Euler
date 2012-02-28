'''
Created on Jul 26, 2011

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.

@author: Admin
'''

def digitequal(n1, n2):
    sn1 = str(n1)
    sn2 = str(n2)
    if len(sn1) != len(sn2):
        return False
    digits = []
    for x in sn1:
        digits.append(x)
    for x in sn2:
        if x in digits:
            digits.remove(x)
        else:
            return False
    return True

if __name__ == "__main__":
    found = False
    # can't start before 123456
    x = 123456
    while not found:
        if (digitequal(x, 2*x) and digitequal(x, 3*x) and digitequal(x, 4*x)
            and digitequal(x, 5*x) and digitequal(x, 6*x)):
            found = True
            print x
        x += 1
        