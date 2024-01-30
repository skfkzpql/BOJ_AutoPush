import sys
a=str(sys.stdin.read().strip())

l=[0]*10
for i in a:
    l[int(i)]+=1

for i in range(9, -1, -1):
    if l[i] != 0:
        print(str(i)*l[i],end='')