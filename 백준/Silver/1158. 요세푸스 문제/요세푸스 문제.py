n,k = map(int,input().split())

l=[i for i in range(1,n+1)]

last_idx = 0

answer = []
for i in range(n):
    pop_idx = (last_idx + k -1) % len(l)
    last_idx = pop_idx
    answer.append(l.pop(pop_idx))

print("<",end='')
print(*answer,sep=", ",end=">")