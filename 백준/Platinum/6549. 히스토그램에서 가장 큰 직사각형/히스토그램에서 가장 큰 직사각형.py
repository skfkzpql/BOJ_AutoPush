f = open(0)

while True:
    N, *histogram = map(int, f.readline().rsplit())
    if N == 0:
        break
        
    stack = []
    max_area = 0

    for i in range(N):
        while stack and histogram[i] < histogram[stack[-1]]:
            height = histogram[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    while stack:
        height = histogram[stack.pop()]
        width = N if not stack else N - stack[-1] - 1
        max_area = max(max_area, height * width)

    print(max_area)