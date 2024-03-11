f = open(0)

while True:
    N, *histogram = map(int, f.readline().rsplit())
    if N == 0: break
    stack = []
    max_area = 0
    histogram.append(0)

    for index in range(N + 1):
        while stack and histogram[index] < histogram[stack[-1]]:
            height = histogram[stack.pop()]
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(index)

    print(max_area)
