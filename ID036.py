'''
Created on Jul 19, 2011

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

@author: Admin
'''

def isPalindrome(word):
    """
    Determines whether a string is a palindrome.
    """
    return word == word[::-1]

if __name__ == "__main__":
    s = 0
    limit = 1000000
    for limit in range(1, limit):
        # bin(num) returns '0b[binary]'. [2:] takes out '0b'.
        if isPalindrome(str(limit)) and isPalindrome(bin(limit)[2:]): s += limit
    print s