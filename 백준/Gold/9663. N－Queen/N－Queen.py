def solve_n_queens(N):
    def backtrack(row, col, ld, rd):
        nonlocal count
        if row == N:
            count += 1
            return
        # 가능한 모든 열에 대해 검사
        available_positions = ~(col | ld | rd) & ((1 << N) - 1)
        while available_positions:
            # 가장 낮은 비트를 가져옴
            p = available_positions & -available_positions
            available_positions -= p
            backtrack(row + 1, col | p, (ld | p) << 1, (rd | p) >> 1)

    count = 0
    backtrack(0, 0, 0, 0)
    return count

# 입력 받기
N = int(input())

# 결과 출력
print(solve_n_queens(N))
