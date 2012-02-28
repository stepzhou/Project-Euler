'''
Created on Jul 26, 2011

How many different ways can 2pounds be made using any number of coins?
1p, 2p, 5p, 10p, 20p, 50p, 1pound (100p) and 2pounds (200p).

Code from Dreamshire.
Introduction to dynamic programming.

@author: Admin
'''

if __name__ == "__main__":
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0] * 200
    
    for coin in coins:
        for n in range(coin, target+1):
            ways[n] += ways[n-coin]
    
    print ways[200]