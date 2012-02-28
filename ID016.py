'''
Created on Jun 16, 2011

What is the sum of the digits of the number 2^1000?

@author: Admin
'''

if __name__ == '__main__':
    # Big ass 2^1000
    num = 2**1000
    sum = 0
    
    while num > 0:
        # Sum adds the ones digit
        sum += num % 10
        
        # Removes the ones place
        num /= 10
        
        # Test
        print "sum: %s num: %s" % (sum, num)
    
    print sum