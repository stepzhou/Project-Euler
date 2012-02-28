'''
Created on Jan 3, 2012

@author: Admin
'''

def is_pandigital(limit):
    s = 9 
    limit=str(limit)
    primes = []
    for d in limit:
        if d == '0': return False
        primes.append(d)
    return len(primes) == s and len(set(primes)) == s

if __name__ == "__main__":
    pandigitals = set()
    for n in xrange(1, 100):
        for j in xrange(2, 10000):
            if is_pandigital(str(n)+str(j)+str(n*j)):
                pandigitals.add(n*j)
                print n, j, n*j
    print sum(set(pandigitals))