import sys

n, *a = sys.stdin.read().splitlines()
l = []
length  = 0
for i in range(int(n)):
    if a[i].startswith('1'):
        l.append(a[i].split()[1])
        length += 1
    elif a[i]=='2':
        if length > 0:
            print(l.pop())
            length -= 1
        else:
            print(-1)
    elif a[i]=='3':
        print(length)
    elif a[i] == '4':
        print('01'[length == 0])
    elif a[i] == '5':
        if length == 0:
            print(-1)
        else:
            print(l[-1])
