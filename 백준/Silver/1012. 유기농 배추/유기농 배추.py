import sys

T = int(sys.stdin.readline())
ans = []
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    terr = [[0] * M for _ in range(N)]

    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        terr[y][x] = 1

    cnt = 0

    for row in range(N):
        for col in range(M):

            if terr[row][col] == 1:
                terr[row][col] = 2
                stack = [(row, col)]
                cnt += 1
                while stack:
                    r, c = stack.pop()

                    if r - 1 >= 0:
                        if terr[r - 1][c] == 1:
                            terr[r - 1][c] = 2
                            stack.append((r - 1, c))

                    if r + 1 < N:
                        if terr[r + 1][c] == 1:
                            terr[r + 1][c] = 2
                            stack.append((r + 1, c))

                    if c - 1 >= 0:
                        if terr[r][c - 1] == 1:
                            terr[r][c - 1] = 2
                            stack.append((r, c - 1))

                    if c + 1 < M:
                        if terr[r][c + 1] == 1:
                            terr[r][c + 1] = 2
                            stack.append((r, c + 1))

    ans.append(cnt)
print(*ans, sep='\n')
