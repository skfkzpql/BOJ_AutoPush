def solve_sudoku(board):
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # 빈 칸이 없으면 스도쿠를 모두 채움
    
    row, col = empty_location
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # 백트래킹
    return False

def find_empty_location(board):
    min_candidates = 10  # 후보군이 가장 적은 셀을 찾기 위해 초기값 설정
    empty_location = None
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                candidates = count_candidates(board, i, j)
                if candidates < min_candidates:
                    min_candidates = candidates
                    empty_location = (i, j)
    return empty_location

def count_candidates(board, row, col):
    candidates = set(range(1, 10))
    for i in range(9):
        candidates.discard(board[row][i])  # 같은 행에 있는 숫자 제거
        candidates.discard(board[i][col])  # 같은 열에 있는 숫자 제거
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            candidates.discard(board[start_row + i][start_col + j])  # 3x3 영역에 있는 숫자 제거
    
    return len(candidates)

def is_safe(board, row, col, num):
    # 행에 중복되는 숫자가 있는지 확인
    if num in board[row]:
        return False
    
    # 열에 중복되는 숫자가 있는지 확인
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # 3x3 영역에 중복되는 숫자가 있는지 확인
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

# 입력 받기
board = []
for _ in range(9):
    row = list(map(int, input().split()))
    board.append(row)

# 스도쿠 풀기
solve_sudoku(board)

# 결과 출력
for row in board:
    print(*row)
