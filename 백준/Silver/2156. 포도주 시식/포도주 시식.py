n, *l = map(int, open(0).read().rsplit())

dp = [0] * n

dp[0] = l[0]

if n > 1:
    dp[1] = l[1] + l[0]
    if n > 2:
        dp[2] = max(l[0] + l[2], l[1] + l[2], dp[1])

        for i in range(3, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + l[i], dp[i - 3] + l[i - 1] + l[i])

print(max(dp))