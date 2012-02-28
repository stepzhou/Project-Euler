'''
Created on Jan 16, 2012

@author: Admin
'''

import timeit

def ID059():
    cipher = open("ID059.txt", "r")
    cipherASCII = file_to_list(cipher)
    ASCII = get_lowercase_ASCII()
    for first in ASCII:
        for second in ASCII:
            for third in ASCII:
                # Imperative to clone else xor is done repeatedly on cipher
                cipherclone = cipherASCII[:]
                key = [first, second, third]
                messageASCII = cyclical_xor(cipherclone, key)
                message = ASCII_to_s(messageASCII)
                # Searches for common words "the" and "and"
                if "the" in message.lower() and "and" in message.lower():
                    print sum(messageASCII), message
                    
def file_to_list(file):
    file_as_str = file.read().split(',')
    return [int(x) for x in file_as_str]

def get_lowercase_ASCII():
    return map(ord,"abcdefghijklmnopqrstuvwxyz")

def ASCII_to_s(li):
    li = [chr(x) for x in li]
    return "".join(li)

def cyclical_xor(nums, key):
    m = len(key)
    for n, x in enumerate(key):
        for j in xrange(n, len(nums), m):
            nums[j] = nums[j] ^ x
    return nums

def test_time():
    TRIALS = 1
    t = timeit.Timer("ID059()", "from __main__ import ID059")
    print "Avg: %.4f s/pass" % (t.timeit(number=TRIALS)/TRIALS)

if __name__ == "__main__":
    ID059()
    test_time()
        