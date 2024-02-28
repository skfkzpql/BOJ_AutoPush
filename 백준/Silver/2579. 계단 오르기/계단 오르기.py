n, *scores = map(int, open(0).read().rsplit())

dp = [0] * (n + 1)

scores.insert(0, 0)

# 초기값 설정
dp[1] = scores[1]
if n > 1:
    dp[2] = scores[1] + scores[2]

# DP 진행
for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i])

print(dp[n])