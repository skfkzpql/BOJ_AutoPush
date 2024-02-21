import sys

N, *histogram = map(int,sys.stdin.read().rsplit())

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