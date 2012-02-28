'''
Created on Jun 16, 2011

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with 
British usage.

@author: Admin
'''

def shave(num):
    """
    Takes off the last digit of a number and returns the new number.
    """
    rem = num % 10
    num /= 10
    
    return num

def writtenoutnumber(num):
    """
    Takes a number and returns the written out form. Currently, is only capable
    with numbers 1-1999.
    """
    # Hard-coding dictionary
    numToWord = {0 : "",
                 1 : "one",
                 2 : "two",
                 3 : "three",
                 4 : "four",
                 5 : "five",
                 6 : "six",
                 7 : "seven",
                 8 : "eight",
                 9 : "nine",
                 10 : "ten",
                 # Weird English cases 11-19
                 11 : "eleven",
                 12 : "twelve",
                 13 : "thirteen",
                 14 : "fourteen",
                 15 : "fifteen",
                 16 : "sixteen",
                 17 : "seventeen",
                 18 : "eighteen",
                 19 : "nineteen",
                 20 : "twenty",
                 30 : "thirty",
                 40 : "forty",
                 50 : "fifty",
                 60 : "sixty",
                 70 : "seventy",
                 80 : "eighty",
                 90 : "ninety",
                 100 : "onehundred",
                 200 : "twohundred",
                 300 : "threehundred",
                 400 : "fourhundred",
                 500 : "fivehundred",
                 600 : "sixhundred",
                 700 : "sevenhundred",
                 800 : "eighthundred",
                 900 : "ninehundred",
                 1000 : "onethousand"}
    
    # oNum = original number. Necessary for tens checking
    oNum = num
    
    ones = num % 10
    num = shave(num)
    
    # Makes sure numbers > 100 read ...eleven instead of ...tenone
    tens = num % 10 * 10
    if tens == 10:
        tens = tens + ones
        ones = 0
    num = shave(num)
    
    hundreds = num % 10 * 100
    num = shave(num)
    
    thousands = num % 10 * 1000
    
    # "and"
    a = ""
    b= ""
    
    # Where the "and" goes for numbers > 100
    if oNum > 100:
        if ones != 0 and tens == 0:
            b = "and"
        elif tens != 0:
            a = "and"
        else:
            pass
        
    # print "ones: %s tens: %s hundreds: %s" % (ones, tens, hundreds)
        
    return numToWord[thousands] + numToWord[hundreds] + a +  numToWord[tens] + b + numToWord[ones]


if __name__ == '__main__':
    sum = 0 
    for x in xrange(1, 1001):
        sum += len(writtenoutnumber(x))
        # print "text: %s \t length: %s" % (writtenoutnumber(x), len(writtenoutnumber(x)))
    
    print sum