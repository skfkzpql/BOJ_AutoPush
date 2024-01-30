a, *b = map(int,open(0).read().split())
c = [25, 10, 5, 1]
l = [[0]*4 for i in range(a)]
for i in range(a):
    m = b[i]
    for j in range(4):
       l[i][j]=m//c[j] 
       m = m%c[j]
    print (*l[i])