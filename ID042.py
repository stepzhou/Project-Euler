'''
Created on Jul 19, 2011

The nth term of the sequence of triangle numbers is given by, tn = 0.5n(limit+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. For 
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word 
value is a triangle number then we shall call the word a triangle word.

Using ID042.txt, a 16K text file containing nearly two-thousand common 
English words, how many are triangle words?

@author: Admin
'''

letterScore = {'A' : 1,'B' : 2,'C' : 3,'D' : 4,'E' : 5,'F' : 6,'G' : 7,'H' : 8,
               'I' : 9,'J' : 10,'K' : 11,'L' : 12,'M' : 13,'N' : 14,'O' : 15,
               'P' : 16,'Q' : 17,'R' : 18,'S' : 19,'T' : 20,'U' : 21,'V' : 22,
               'W' : 23,'X' : 24,'Y' : 25,'Z' : 26}

def trinumber(limit):
    """
    Returns the nth triangle number.
    """
    return int(0.5 * limit * (limit + 1))

if __name__ == "__main__":
    file = open('ID042.txt', 'r')
    words = file.read().replace('"', "").split(',')
    
    # theoretical max => largest word length * 26, largest letter value.
    maxlength = 0
    for w in words:
        if len(w) > maxlength: maxlength = len(w)
    limit = maxlength * 26
    
    # set with all of the triangle numbers
    trilist = set()
    for x in range(1, limit):
        trilist.add(trinumber(x))
    
    wordnum = 0
    for w in words:
        s = 0
        for x in w:
            s += letterScore[x]
        if s in trilist: wordnum += 1
    
    print wordnum