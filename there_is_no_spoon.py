import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lines = []
columns = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    lines.append(line)
    #print("values: ", line, file=sys.stderr)

for i in range(width):
    column = ""
    for line in lines:
        column += line[i]
    columns.append(column)

print("lines: ", lines, file=sys.stderr)
print("columns: ", columns, file=sys.stderr)
    
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

for i in range(width):
    for j in range(height):
        currentNode = ""
        nodeRight = ""
        nodeBottom = ""
        nodeValue = lines[j][i]
        rightNodes = findOccurrences(lines[j], "0")
        bottomNodes = findOccurrences(columns[i], "0")
        if nodeValue == "0":
            currentNode = "{0} {1}".format(i, j)
            if i == width - 1:
                nodeRight = "-1 -1"
            else:
                for index in rightNodes:
                    if index > i:
                        nodeRight = "{0} {1}".format(index, j)
                        break
                    else:
                        nodeRight = "-1 -1"



            if j == height - 1:
                nodeBottom = "-1 -1"
            else:
                for index in bottomNodes:
                    if index > j:
                        nodeBottom = "{0} {1}".format(i, index)
                        break
                    else:
                        nodeBottom = "-1 -1"
            #print("nodeCurrent", currentNode, file=sys.stderr)
            #print("nodeRight", nodeRight, file=sys.stderr)
            #print("nodeBottom", nodeBottom, file=sys.stderr)
            #print(nodeRight)
            print("{0} {1} {2}".format(currentNode, nodeRight, nodeBottom))
                
            
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# Three coordinates: a node, its right neighbor, its bottom neighbor