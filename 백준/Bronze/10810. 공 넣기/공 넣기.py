a , b = map(int,input().split())
la = [0]*a

for i in range(b):
    c, d, e = map(int,input().split())
    la[c-1:d] = [e]*(d-c+1)

print(*la)