import sys
a = int(sys.stdin.readline().rstrip())
for i in range(a):
    b, c = map(int,sys.stdin.readline().rstrip().split())
    d = b+c
    print(f'Case #{i+1}: {b} + {c} = {d}')