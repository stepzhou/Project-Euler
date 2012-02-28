'''
Created on Jan 4, 2012

@author: Admin
'''

square_cache = {0:0, 1:1, 89:89}
marked = [0]*10000000
marked[1] = 1
marked[89] = 89

def sum_square_digits(limit):
    limit = str(limit)
    s = 0
    for c in limit:
        s += int(c)**2
    return s

def mark(limit):
    if marked[limit] == 0:
        return limit
    return marked[limit]

if __name__ == "__main__":
    limit = 10000000
    count = 0
    for n in xrange(2, limit):
        num = n
        while num != 1 and num != 89:
            num = sum_square_digits(num)
            num = mark(num)
        marked[n] = num
        if num == 89:
            count += 1
    print count