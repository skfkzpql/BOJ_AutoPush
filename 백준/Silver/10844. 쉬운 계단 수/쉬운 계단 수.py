n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for length in range(2, n + 1):
    for digit in range(10):
        if digit - 1 >= 0:
            dp[length][digit] += dp[length - 1][digit - 1]
        if digit + 1 <= 9:
            dp[length][digit] += dp[length - 1][digit + 1]
        dp[length][digit] %= 1e9

print(int(sum(dp[n]) % 1e9))
