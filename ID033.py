'''
Created on Jan 2, 2012

@author: Admin
'''

def has_same_digit(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    
    for ch1 in num1_str:
        for ch2 in num2_str:
            if ch1 == ch2:
                return True
    return False

def get_simplified_fraction(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    
    for ch1 in num1_str:
        for ch2 in num2_str: 
            if ch1 == ch2:
                num1_str = num1_str.replace(ch1, "")
                num2_str = num2_str.replace(ch2, "")
    
    # Dirty error-handling
    if num1_str == "" or num2_str == "" or num2_str == "0":
        return 0.0
    return float(num1_str)/float(num2_str)

if __name__ == "__main__":
    N_END = 99
    
    d_start = 11
    n_start = 12
    d = d_start
    limit = n_start
    
    while d <= N_END-1:
        while limit <= N_END:
            if has_same_digit(d, limit):
                simplified = get_simplified_fraction(d, limit)
                actual = float(d) / limit
                if simplified == actual:
                    print d, limit
            limit += 1
        d += 1
        limit = d + 1
        
    # 16/64, 19/95, 26/65, 49/98