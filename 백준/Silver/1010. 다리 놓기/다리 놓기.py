import math
import sys

T = int(sys.stdin.readline())
COUNT = 0
for _ in range(T):
    n, m = map(int, sys.stdin.readline().rsplit())
    print(math.comb(m,n))