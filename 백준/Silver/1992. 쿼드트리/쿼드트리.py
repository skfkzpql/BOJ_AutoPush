def compress_quad_tree(x, y, size, image):
    cur = image[x][y]

    if all(image[i][j] == image[x][y] for i in range(x, x + size) for j in range(y, y + size)):
        return cur

    half = size // 2
    upper_left = compress_quad_tree(x, y, half, image)
    upper_right = compress_quad_tree(x, y + half, half, image)
    lower_left = compress_quad_tree(x + half, y, half, image)
    lower_right = compress_quad_tree(x + half, y + half, half, image)

    return "(" + upper_left + upper_right + lower_left + lower_right + ")"


if __name__ == "__main__":
    f = open(0)
    N = int(f.readline())
    image = [f.readline().rstrip() for _ in range(N)]

    print(compress_quad_tree(0, 0, N, image))