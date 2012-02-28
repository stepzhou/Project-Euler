'''
Created on Jul 5, 2011

How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?

@author: Admin
'''

if __name__ == "__main__":   
    years = []
    n = 1900
    while n <= 2000:
        if n % 4 == 0 and n != 1900:
            years.append(366)
        else:
            years.append(365)
        n += 1
    
    sundays = []
    day = 7
    for x in years:
        oneyear = []
        while day <= x:
            oneyear.append(day)
            day += 7
        day = 7 - (x - oneyear[-1])
        sundays.append(oneyear)
    print sundays
    
    n = 1
    limit = 0
    monthstartreg = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    monthstartleap = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
    while n <= 100:
        if n % 4 == 0 and n != 0:
            for x in monthstartleap:
                if x in sundays[n]: limit += 1
        else:
            for x in monthstartreg: 
                if x in sundays[n]: limit += 1
        n += 1

    print limit
    
    # Or you could just be a smart pants and do 100*12/7