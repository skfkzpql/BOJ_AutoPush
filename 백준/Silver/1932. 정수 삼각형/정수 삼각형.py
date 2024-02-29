f = open(0).readlines()
n = int(f[0])
l = [list(map(int, f[i].split())) for i in range(1, n + 1)]

dp = [[0] * i for i in range(1, n)]
dp.append(l[-1])

for i in range(n-2, -1, -1):
    for j in range(i+1):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + l[i][j]


print(dp[0][0])