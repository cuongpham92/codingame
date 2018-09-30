import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r_1 = int(input())
r_2 = int(input())

# First approach
min_num = min(r_1, r_2)
max_num = max(r_1, r_2)

def next_num(r):
    return r + sum(map(int, str(r)))

while True:
    while min_num < max_num:
        min_num = next_num(min_num)
    if max_num != min_num:
        max_num = next_num(max_num)
    else:
        print(max_num)
        break
    
'''
# Second approach: using binary search
def next_num(r):
    return r + sum(map(int, str(r)))

def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        mid = int((first+last)/2)
        if alist[mid] == item:
            found = True
            print(alist[mid])
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return found

list_r1 = [r_1]
list_r2 = [r_2]
while True:
    r_1 = next_num(r_1)
    list_r1.append(r_1)
    if binary_search(list_r1, r_2) == True:
        break
    r_2 = next_num(r_2)
    list_r2.append(r_2)
    if binary_search(list_r2, r_1) == True:
	    break
'''