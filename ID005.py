'''
Created on Jun 13, 2011

Finds the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20.

@author: Stephen Zhou
'''

if __name__ == '__main__':
    nums = range(1,20)[::-1]
    
    count = 0
    go = True
    
    while go == True:
        count += 20
        for x in nums:
            if (count % x != 0):
                go = True
                break
            else:
                go = False  
    
    print count