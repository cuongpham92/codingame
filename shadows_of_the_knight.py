import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.

w, h = [int(i) for i in input().split()]
#print("abced", w, h, file=sys.stderr)
n = int(input())  # maximum number of turns before game over.
#print("abced", n, file=sys.stderr)
x, y = [int(i) for i in input().split()]
#print("abced", x0, y0, file=sys.stderr)

x1 = 0
y1 = 0
x2 = w - 1
y2 = h - 1
#print(x_temp, y_temp, file=sys.stderr)
    
while True:
    bomb_dir = input()

    if "U" in bomb_dir:
        y2 = y - 1
    elif "D" in bomb_dir:
        y1 = y + 1

    if "L" in bomb_dir:
        x2 = x - 1
    elif "R" in bomb_dir:
        x1 = x + 1

    x = int(x1 + (x2 - x1) / 2);
    y = int(y1 + (y2 - y1) / 2);
    print(x, y)
      