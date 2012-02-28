'''
Created on Jun 14, 2011

Finds the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.

@author: Admin
'''

if __name__ == '__main__':
    limit = 100
    
    
    sumSquare = 0
    
    for x in range(0, limit+1):
        sumSquare += x * x
    
    squareSum = 0
    
    for x in range(0, limit+1):
        squareSum += x
    
    squareSum *= squareSum
    
    print squareSum - sumSquare