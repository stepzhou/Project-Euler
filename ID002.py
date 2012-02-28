'''
Created on Jun 11, 2011

Only considers the values of the Fibonacci sequence whose values do not exceed
4 million and sums the even-valued terms.

@author: Stephen Zhou
'''

class Fibonacci:
    
    def __init__(self):
        self.data = []
        self.one = 1
        self.two = 1
    
    def next(self):
        sum = self.one + self.two
        self.one = self.two
        self.two = sum
        return sum

if __name__ == '__main__':
    
    fib = Fibonacci()
    current = 1
    sum = 0
    
    while current < 4000000:
        if (current % 2 == 0):
            sum += current
        current = fib.next()       
    
    print sum