def dfs(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(1, N + 1):
        if i in out:
            continue
        out.append(i)
        dfs(depth + 1, N, M)
        out.pop()

N, M = map(int, input().split())
out = []
dfs(0, N, M)
