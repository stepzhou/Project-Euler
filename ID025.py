'''
Created on Jun 21, 2011
Completed on Jun 21, 2011

What is the first term in the Fibonacci sequence to contain 1000 digits?

@author: Admin
'''

# cache of fib pairs. "memorization" technique
memo = {0:0, 1:1}

def F(limit):
    """
    Returns the nth term in the fib sequence. bypasses memory-intensive
    recursion by having a dictionary of stored fib sequence pairs.
    """
    if limit not in memo:
        memo[limit] = F(limit-1) + F(limit-2)
    return memo[limit]

if __name__ == '__main__':
    limit = 1
    fib = F(limit)
    # 10^999 is the first 1000 digit number
    while fib < 10 ** 999:
        limit += 1
        fib = F(limit)
    
    print limit