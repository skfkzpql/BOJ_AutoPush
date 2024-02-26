import sys
from collections import deque

MAX_VALUE = 1000000

N, *l = map(int, sys.stdin.read().rsplit())

l = deque(l)
dp = [0]*MAX_VALUE.bit_length()

for i in range(N):
    a = l.pop()
    for s in range(a.bit_length()):
        dp[s] += a >> s & 1

answer = 0
power_of_2 = 1

for i in range(len(dp)):
    a = dp[i]
    answer += (power_of_2 << i) * a * (N-a)

print(answer)