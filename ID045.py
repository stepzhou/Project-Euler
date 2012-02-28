'''
Created on Jul 21, 2011

Find the next triangle number that is also pentagonal and hexagonal after 
40755

@author: Admin
'''

def hexgen(x):
    return x * (2*x - 1)

def trigen(x):
    return (x * (x + 1)) / 2

def pentgen(x):
    return (x * (3*x - 1)) / 2

if __name__ == "__main__":
    notfound = True
    h = 143
    p = 165
    t = 285
    while notfound:
        h += 1
        hex = hexgen(h)
        
        t += 1
        tri = trigen(t)
        while tri < hex:
            t += 1
            tri = trigen(t)
        
        p += 1
        pent = pentgen(p)
        while pentgen(p) < hex:
            p += 1
            pent = pentgen(p)
        
        if hex == tri == pent:
            notfound = False
            print hex, tri, pent
        
