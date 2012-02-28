'''
Created on Jun 17, 2011

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
Numbers are stored in file ID013.txt

@author: Admin
'''

if __name__ == '__main__':
    f = open("ID013.txt", "r")
    sum = 0
    count = 0
    for line in f:
        count += 1
        sum += long(line)
        print "#: %3d sum: %d" % (count, sum)
        
    f.close()
    
    print sum
    strsum = str(sum)
    str = ""
    
    for x in xrange(10):
        str += strsum[x]
        
    print str
    
