def dfs(start, depth, N, M):
    if depth == M:
        print(' '.join(map(str, sequence)))
        return
    for i in range(start, N + 1):
        sequence.append(i)
        dfs(i, depth + 1, N, M)  # 다음 숫자는 현재 숫자보다 크거나 같아야 하므로, start를 i로 설정
        sequence.pop()

N, M = map(int, input().split())
sequence = []
dfs(1, 0, N, M)
