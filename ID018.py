'''
Created on Jul 5, 2011

Find the maximum total from top to bottom of the triangle.

@author: Admin
'''

file = open("ID018.txt", "r")
triangle = []
for line in file:
    triangle.append(line.rstrip("\n").split(" "))

# Convert list strings to int
triangle = [map(int, x) for x in triangle]

if __name__ == '__main__':    
    line = 0
    while line < len(triangle)-1:
        row = [0]
        # for loop with index using enumerate
        for idx, x in enumerate(triangle[line]):
            # d is down; dr is down-right
            d = x + triangle[line+1][idx]
            dr = x + triangle[line+1][idx+1]
            if d > row[idx]:
                row[idx] = d
            row.append(dr)
        # replace following row with summed row
        triangle[line+1] = row
        line += 1
    
    print max(triangle[-1])