a, b = open(0).read().rsplit()
m = len(a) + 1
n = len(b) + 1
dp = [[0] * n for _ in range(m)]

for i in range(1, m):
    for j in range(1, n):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
