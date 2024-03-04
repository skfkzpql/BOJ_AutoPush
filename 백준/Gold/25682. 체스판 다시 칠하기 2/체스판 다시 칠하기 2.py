f = open(0)
N, M, K = map(int, f.readline().rsplit())
board = [f.readline().rstrip() for _ in range(N)]


def calculate_prefix_sum():
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

            if (i + j) % 2 == 0:
                if board[i - 1][j - 1] == 'W':
                    prefix_sum[i][j] += 1
            else:
                if board[i - 1][j - 1] == 'B':
                    prefix_sum[i][j] += 1

    return prefix_sum

def count_changes(x1, y1, x2, y2):
    return prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]

prefix_sum = calculate_prefix_sum()
min_changes = float('inf')

for i in range(K, N + 1):
    for j in range(K, M + 1):
        changes = count_changes(i - K + 1, j - K + 1, i, j)
        min_changes = min(min_changes, changes, K * K - changes)

print(min_changes)
