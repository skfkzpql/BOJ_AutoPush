import math
import sys

N = int(sys.stdin.readline().rstrip())

s = set()

count = 0

for i in range(N):
    line = sys.stdin.readline().rstrip()
    if line == 'ENTER':
        count += len(s)
        s = set()
    else:
        s.add(line)
    if i == N-1:
        count += len(s)

print(count)
    