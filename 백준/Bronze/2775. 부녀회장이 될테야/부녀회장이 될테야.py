t = int(input())

dp = [[0] * 15 for _ in range(15)]

for i in range(15):
    dp[0][i] = i + 1
    dp[i][0] = 1

for i in range(1,15):
    for j in range(1, 15):
        dp[i][j] += dp[i][j-1] + dp[i-1][j]

for i in range(t):
    n = int(input())
    k = int(input())
    
    print(dp[n][k-1])