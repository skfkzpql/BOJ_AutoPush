import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().rsplit()))
c = list(map(int, sys.stdin.readline().rsplit()))[:-1]

min_cost = c[0]
cost = c[0]*l[0]

for i in range(1,n -1):
    min_cost = min(min_cost, c[i])
    cost += l[i] * min_cost

print(cost)