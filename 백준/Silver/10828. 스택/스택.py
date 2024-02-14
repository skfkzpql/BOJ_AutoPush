import sys

_, *l = sys.stdin.read().splitlines()

stack = []

for i in l:
    c = i.split()
    if c[0] == "push":
        stack.append(c[1])
    elif c[0] == "pop":
        print(stack.pop() if stack else -1)
    elif c[0] == "size":
        print(len(stack))
    elif c[0] == "empty":
        print(int(not stack))
    else:
        print(stack[-1] if stack else -1)
