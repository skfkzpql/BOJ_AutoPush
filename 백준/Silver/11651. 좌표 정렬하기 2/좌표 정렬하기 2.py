import sys
a, *data=map(int,sys.stdin.read().rsplit())

l=[(int(data[i]),int(data[i+1])) for i in range(0,len(data),2) ]

b=sorted(l,key=lambda k: (k[1],k[0]))
for i in range(len(b)):
    print(b[i][0],b[i][1])