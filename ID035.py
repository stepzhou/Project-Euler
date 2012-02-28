'''
Created on Jul 10, 2011
Completed on Jul 13, 2011

How many circular check_prime are there below one million?

@author: Admin
'''

def sieveOfErat(end):  
    if end < 2: return []  

    # The array doesn't need to include even numbers  
    lng = ((end/2)-1+end%2)  
    
    # Create array and assume all numbers in array are prime  
    sieve = [True]*(lng+1)  
    
    # In the following code, you're going to see some funky  
    # bit shifting and stuff, this is just transforming n and j  
    # so that they represent the proper elements in the array.  
    # The transforming is not optimal, and the number of  
    # operations involved can be reduced.  
  
    # Only go up to square root of the end  
    for n in range(int(end**0.5) >> 1):  
        # Skip numbers that aren't marked as prime
        if not sieve[n]: continue  

        # Unmark all multiples of n, starting at n**2  
        for j in range( (n*(n + 3) << 1) + 3, lng, (n << 1) + 3):  
            sieve[j] = False  

    # Don't forget 2!  
    check_prime = [2]  

    # Gather all the check_prime into a list, leaving out the composite numbers  
    check_prime.extend([(n << 1) + 3 for n in range(lng) if sieve[n]])  

    return check_prime

def findcircular(num):
    """
    Returns a list of a number's rotations.
    197: 197, 971, 719
    101: 101, 110
    """
    snum = str(num)
    circs = []
    if len(snum) == 1:
        return [num]
    else:
        for n in range(len(snum)):
            if int(snum[0]) != 0:
                circs.append(int(snum))
            snum = snum[1:] + snum[0]
        return circs

if __name__ == "__main__":
    limit = 1000000
    check_prime = set(sieveOfErat(limit))
    circular = []
    
    for p in check_prime:
        count = 0
        circs = findcircular(p)
        for x in circs:
            if x in check_prime: count += 1
        if count == len(circs): circular.append(p)
        # print p
            
    print len(circular)