f = open(0)

n, m = map(int, f.readline().rsplit())
board = [[0]*(n+1)]
for i in range(n):
    l = [0] + list(map(int, f.readline().rsplit()))
    for j in range(1, n+1):
        l[j] += l[j-1]
    for j in range(1, n+1):
        l[j] += board[-1][j]
    board.append(l)

for i in range(m):
    x1, y1, x2, y2 = map(int, f.readline().rsplit())
    print(board[x2][y2] - board[x1-1][y2] - board[x2][y1 - 1] + board[x1 - 1][y1 - 1])