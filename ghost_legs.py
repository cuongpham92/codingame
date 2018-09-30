import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
tops = []
bottoms = []
body = []
for i in range(h):
    line = input()
    if i == 0:
        tops = line
    elif i == h-1:
        bottoms = line
    else:
        body.append(line)

#print(tops, file=sys.stderr)
#print(bottoms, file=sys.stderr)
#print(body, file=sys.stderr)

for i in range(0, len(tops)):
    if tops[i] != " ":
        bottom_col = i
        for j in range(0, len(body)):
            #print("starting loop: ", bottom_col, file=sys.stderr)
            if bottom_col == len(tops)-1:
                if body[j][bottom_col-1] == "-":
                    bottom_col -= 3
                    #print("inside loop: ", bottom_col, file=sys.stderr)
            else:
                if body[j][bottom_col+1] == "-":
                    bottom_col += 3
                    #print("inside loop: ", bottom_col, file=sys.stderr)
                elif body[j][bottom_col-1] == "-":
                    bottom_col -= 3
                    #print("inside loop: ", bottom_col, file=sys.stderr)
        print("{0}{1}".format(tops[i], bottoms[bottom_col]))
                
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

#print("answer")