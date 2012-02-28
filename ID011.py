'''
Created on Jun 16, 2011
Completed on Jun 20, 2011

What is the greatest product of four adjacent numbers in any direction 
(up, down, left, right, or diagonally) in the 2020 grid?

@author: Admin
'''

file = open("ID011.txt", "r")
m = []
for line in file:
    list = [int(x) for x in line.split(" ")]
    m.append(list)
file.close() 

def checkvert():
    """
    Returns the largest vertical products
    """
    biggest = 0
    for row in range(len(m)-3):
        for col in range(len(m[0])):
            vert = m[row][col] * m[row+1][col] * m[row+2][col] * m[row+3][col]
            if vert > biggest:
                biggest = vert
    
    return biggest            

def checkhoriz():
    """
    Returns the largest horizontal products
    """
    biggest = 0
    for row in range(len(m)):
        for col in range(len(m[0])-3):
            hor = m[row][col] * m[row][col+1] * m[row][col+2] * m[row][col+3]
            if hor > biggest:
                biggest = hor
    
    return biggest  

def checkdiag():
    """
    Returns the largest diagonal products
    """
    # Diagonals from top left to bottom right
    biggest = 0
    for row in range(len(m)-3):
        for col in range(len(m[0])-3):
            right = m[row][col] * m[row+1][col+1] * m[row+2][col+2] * m[row+3][col+3]
            if right > biggest:
                biggest = right
    
    # Diagonals from top right to bottom left
    for row in range(len(m)-3):
        for col in range(3, len(m))[::-1]:
            left = m[row][col] * m[row+1][col-1] * m[row+2][col-2] * m[row+3][col-3]
            if left > biggest:
                biggest = left
    
    return biggest  

if __name__ == '__main__':
    values = [checkvert(), checkhoriz(), checkdiag()]
    print "The maximum product is: " + str(max(values))