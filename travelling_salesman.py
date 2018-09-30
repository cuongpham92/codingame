import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
xs = []
ys = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    xs.append(x)
    ys.append(y)

visited = []
for i in range(0, len(xs)):
    visited.append(0)

print(xs, file=sys.stderr)
print(ys, file=sys.stderr)
def euclid_dis(x1, y1, x2, y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

total_dis = 0
start_point = 0
step = n

while step > 1:
    print(visited, file=sys.stderr)
    shortest_dis = 1000000
    shortest_city_index = 0
    
    for j in range(1, n):
        if visited[j] == 0:
            dis = euclid_dis(xs[start_point], ys[start_point], xs[j], ys[j])
            print("euclid dis: ", start_point, j, dis, file=sys.stderr)
            if dis < shortest_dis:
                shortest_dis = dis
                shortest_city_index = j
            
    print("shortest dis: ", shortest_dis, file=sys.stderr)
    
    if shortest_dis == 1000000:
        shortest_dis = 0
    visited[shortest_city_index] = 1
    start_point = shortest_city_index
    step -= 1
    total_dis += shortest_dis
    print("start point: ", start_point, file=sys.stderr)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
last_dis = euclid_dis(xs[start_point], ys[start_point], xs[0], ys[0])
print(last_dis, file=sys.stderr)
total_dis += last_dis
print(int(round(total_dis)))