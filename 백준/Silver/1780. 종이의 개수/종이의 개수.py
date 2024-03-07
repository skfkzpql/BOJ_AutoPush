def compress_quad_tree(size, image):
    stack = [(0, 0, size)]
    cnt = [0, 0, 0]
    while stack:
        x, y, s = stack.pop()

        if all(image[i][j] == image[x][y] for i in range(x, x + s) for j in range(y, y + s)):
            cnt[image[x][y]] += 1
        else:
            one_third = s // 3
            for i in range(3):
                for j in range(3):
                    stack.append((x+(one_third*i), y+(one_third*j), one_third))


    print(cnt[-1], cnt[0], cnt[1], sep='\n')


if __name__ == "__main__":
    f = open(0)
    N = int(f.readline())
    image = [list(map(int, f.readline().rsplit())) for _ in range(N)]

    compress_quad_tree(N, image)
