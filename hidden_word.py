import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
print(n, file=sys.stderr)
words = []
for i in range(n):
    aword = input()
    words.append(aword)
    #print(aword, file=sys.stderr)
print("words: ", words, file=sys.stderr)

h, w = [int(i) for i in input().split()]
grid = []
print("h, w: ", h, w, file=sys.stderr)
for i in range(h):
    line = input()
    grid.append(line)
    #print(line, file=sys.stderr)

print("grid", grid, file=sys.stderr)

# Initiate a matrix
matrix = []
for i in range(0, h):
    l = []
    for j in range(0, w):
        l.append(0)
    matrix.append(l)


# Coordinate of 8 directions from perspective of current cell
x = [-1, -1, -1, 0, 0, 1, 1, 1] 
y = [-1, 0, 1, -1, 1, -1, 0, 1]

def find_word(aword, grid, h, w, row, col):
    direction = -1
    
    # If first character of word doesnt match the starting point of grid
    if grid[row][col] is not aword[0]:
        return direction
    
    #Search word in all 8 directions starting from (row,col)
    for try_dir in range(0, 8):
        found_word = True
        # First character is already checked, match remaining characters
        for j in range(1, len(aword)):
            
            # Moving in particular direction
            next_row = row + j*x[try_dir]
            next_col = col + j*y[try_dir]
            
            #If out of bound break
            if next_row < 0 or next_row >= h or next_col < 0 or next_col >= w:
                found_word = False
                break
            
            # If not matched,  break
            if grid[next_row][next_col] is not aword[j]:
                found_word = False
                break
    
        if found_word == True:
            direction = try_dir
            return direction
    
    return direction
            
    
                    
for aword in words:
    for row in range(0, w):
        for col in range(0, h):
            direction = find_word(aword, grid, h, w, row, col)
            if direction != -1: 
                for j in range(0, len(aword)):
                    next_row = row + j*x[direction]
                    next_col = col + j*y[direction]
                    matrix[next_row][next_col] = 1
               
answer = ""
for i in range(0, h):
    for j in range(0, w):
        if matrix[i][j] == 0:
            answer += grid[i][j]
print(answer)
