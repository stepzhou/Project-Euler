'''
Created on Jun 20, 2011

INCOMPLETE

@author: Admin
'''

# TODO: how to not define each hundred?
numberMap = (('onethousand', 1000),
             ('ninehundred', 900),
             ('eighthundred', 800),
             ('sevenhundred', 700),
             ('sixhundred', 600),
             ('fivehundred', 500),
             ('fourhundred', 400),
             ('threehundred', 300),
             ('twohundred', 200),
             ('onehundred', 100),
             ('ninety', 90),
             ('eighty', 80),
             ('seventy', 70),
             ('sixty', 60),
             ('fifty', 50),
             ('forty', 40),
             ('thirty', 30),
             ('twenty', 20),
             ('nineteen', 19),
             ('eighteen', 18),
             ('seventeen', 17),
             ('sixteen', 16),
             ('fifteen', 15),
             ('fourteen', 14),
             ('thirteen', 13),
             ('twelve', 12),
             ('eleven', 11),
             ('ten', 10),
             ('nine', 9),
             ('eight', 8),
             ('seven', 7),
             ('six', 6),
             ('five', 5),
             ('four', 4),
             ('three', 3),
             ('two', 2),
             ('one', 1))


def toWords(limit):
    result = ""
    for word, integer in numberMap:
        while limit >= integer:
            result += word
            limit -= integer
    
    #TODO: "and" is a bitch
    a = "and"
    
    
    return result

if __name__ == '__main__':
    print toWords(1322)