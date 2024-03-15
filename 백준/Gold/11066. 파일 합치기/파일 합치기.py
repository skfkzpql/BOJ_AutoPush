f = open(0)

T = int(f.readline())

for case in range(T):
    K = int(f.readline())
    files = list(map(int, f.readline().rsplit()))

    dp = [[0] * K for _ in range(K)]

    # 누적합 구하기
    cumulative_dict = {0:0}
    total_sum = 0
    for idx, num in enumerate(files,1):
        total_sum += num
        cumulative_dict[idx] = total_sum

    #print(cumulative_dict)
    for length in range(2, K+1):
        for start in range(K-length + 1):
            minimum = int(1e9)
            for end in range(length - 1):
                #print(f"length: {length}, start:{start}, end:{end} dp[{start}][{start + length - 1}] = min(dp[{start}][{start + end}], dp[{start + end + 1}][{start + length - 1}]) + cumulative_dict[{start + length}] - cumulative_dict[{start}]")
                minimum = min(dp[start][start+end] + dp[start+end+1][start+length-1], minimum)

            dp[start][start+length - 1] += minimum + cumulative_dict[start+length] - cumulative_dict[start]

    print(dp[0][K-1])
