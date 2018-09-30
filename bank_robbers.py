import sys
import math
import bisect

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def time_solve_vault(c, n):
    return 10**n * 5**(c-n)

total_time = 0
r = int(input())
v = int(input())
#print(r, v, file=sys.stderr)

time_solve_list = []
for i in range(v):
    c, n = [int(j) for j in input().split()]
    print(c, n, file=sys.stderr)
    time_solve = time_solve_vault(c, n)
    time_solve_list.append(time_solve)

total_time_solve = 0
current_vault_list = []

for i in range(0, r):
    bisect.insort(current_vault_list, time_solve_list[i])

#print(current_vault_list, file=sys.stderr)

if r == v:
    total_time_solve = current_vault_list[-1]

else:
    
    count = 1
    #print("count total: ", int(v/r + 1), file=sys.stderr)
    while True:
        if count > int(v - r + 1):
            break
        
        #print("count: ", count, file=sys.stderr)
        #print("current vault list: ", current_vault_list, file=sys.stderr)
        
        temp = current_vault_list[0]
        current_vault_list.pop(0)
        
        for i in range(0, len(current_vault_list)):
            current_vault_list[i] -= temp
        
        if count < int(v - r + 1):
            bisect.insort(current_vault_list, time_solve_list[r + count - 1])
            
        total_time_solve += temp
        #print("current vault list: ", current_vault_list, file=sys.stderr)
        #print("current total_time_solve: ", total_time_solve, file=sys.stderr)
        
        count += 1
    total_time_solve += current_vault_list[-1]

print(total_time_solve)