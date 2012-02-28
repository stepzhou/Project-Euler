'''
Created on Jan 3, 2012

@author: Admin
'''

if __name__ == "__main__":
    """
    Algorithm from:
    http://www.exploringbinary.com/how-to-find-the-last-digits-of-a-positive-power-of-two/
    3. Cyclic Powers
        Finding the Last m Digits
        
    Go there for more information on number theory
    """
    coefficient = 28433
    limit = 7830457
    m = 10
    j = (limit-m) % (4*5**(m-1))
    base = 2**(m+j)
    print str(coefficient*base+1)[-10:]
