def count_color_paper(x, y, r, c, board):
    tmp_cnt_b = 0
    tmp_cnt_w = 0
    for i in range(x, r):
        for j in range(y, c):
            if board[i][j] == 1:
                tmp_cnt_b += 1
            else:
                tmp_cnt_w += 1
    return tmp_cnt_w, tmp_cnt_b


def cut_paper(x, y, r, c, board):
    global cnt_w, cnt_b
    tmp_cnt_w, tmp_cnt_b = count_color_paper(x, y, r, c, board)

    if tmp_cnt_w == (r - x) ** 2:
        cnt_w += 1
    elif tmp_cnt_b == (r - x) ** 2:
        cnt_b += 1
    else:
        if (r - x) != 1:
            dx = (r - x) // 2
            cut_paper(x, y, x + dx, y + dx, board)
            cut_paper(x + dx, y, r, y + dx, board)
            cut_paper(x, y + dx, x + dx, c, board)
            cut_paper(x + dx, y + dx, r, c, board)


f = open(0)
n = int(f.readline())
board = [list(map(int, f.readline().rsplit())) for _ in range(n)]

cnt_b = 0
cnt_w = 0

cut_paper(0, 0, n, n, board)

print(cnt_w)
print(cnt_b)
