'''
Created on Jun 13, 2011

@author: Admin
'''

if __name__ == '__main__':
    d = 3
    limit = 600851475143
    while (d * d < limit): 
        if limit % d == 0: limit /= d 
        else: d += 2 
        print str(d) + " " + str(limit)
    print limit 
