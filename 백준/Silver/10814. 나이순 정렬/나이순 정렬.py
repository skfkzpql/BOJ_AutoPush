import sys
a,*l=sys.stdin.read().rsplit()
b=[]

for i in range(int(a)):
    b.append((int(l[2*i]),l[2*i+1],i))

b.sort(key=lambda x: (x[0],x[2]))

for i in range(int(a)):
    print(b[i][0],b[i][1])