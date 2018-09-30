import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
loss = -1
values = []
for i in input().split():
    v = int(i)
    values.append(v)
    
loss = 0

currentMax = values[0]
currentMin = values[0]

for i in range(1, len(values)):
    if values[i] < values[i-1]:
        if values[i] < currentMin:
            currentMin = values[i]
    
    if values[i] > values[i-1]:
        if values[i] > currentMax:
            currentMax = values[i]
            currentMin = values[i]
    
    tmp_loss = currentMin - currentMax
            
    if tmp_loss < loss:
        loss = tmp_loss
            #print("tmp_loss: ", tmp_loss, file=sys.stderr)
            #print("loss: ", loss, file=sys.stderr)

print(loss)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)