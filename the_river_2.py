import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r_1 = int(input())
print(r_1, file=sys.stderr)

next_num = lambda r: r + sum(map(int, str(r)))

step = 9*len(str(r_1))

count = 0
for i in range(1, step):
	if i < r_1:
		num = r_1 - i
		if (next_num(num)) == r_1:
			print("YES")
			sys.exit()

print("NO")

