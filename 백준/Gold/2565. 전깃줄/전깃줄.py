l = [tuple(map(int, line.split())) for line in open(0).readlines()[1:]]
n = len(l)

l.sort()
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if l[i][1] > l[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))