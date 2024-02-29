n = int(input())
l = list(map(int, input().split()))

dp = [-1000] * (n+1)
dp[1] = l[0]

for i in range(2, n + 1):
    dp[i] = max(dp[i-1] + l[i-1], l[i-1])

print(max(dp))