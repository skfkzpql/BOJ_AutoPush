def solution(n):
    if n % 2 == 1:  # n이 홀수인 경우 타일로 채울 수 없으므로 0 반환
        return 0
    
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0], dp[2] = 1, 3
    for i in range(4, n + 1, 2):
        dp[i] = dp[i-2] * 3 + 2 * sum(dp[:i-2]) % MOD
    
    return dp[n] % MOD
