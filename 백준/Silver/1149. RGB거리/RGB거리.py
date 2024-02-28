n, *l = open(0).readlines()
n = int(n)
costs =[]
for i in l:
    r, g, b = map(int, i.split())
    costs.append([r,g,b])


dp = [[0] * 3 for _ in range(n)]
dp[0] = costs[0]

RED, GREEN, BLUE = 0, 1, 2

for i in range(1, n):
    dp[i][RED] = min(dp[i-1][GREEN], dp[i-1][BLUE]) + costs[i][RED]
    dp[i][GREEN] = min(dp[i-1][RED], dp[i-1][BLUE]) + costs[i][GREEN]
    dp[i][BLUE] = min(dp[i-1][RED], dp[i-1][GREEN]) + costs[i][BLUE]

print(min(dp[-1]))