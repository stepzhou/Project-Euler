'''
Created on Jun 17, 2011

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

@author: Admin
'''

if __name__ == '__main__':
    s = sum(x**x for x in range(1, 1001))
        
    print str(s)[-10:]