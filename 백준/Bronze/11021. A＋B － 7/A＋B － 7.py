import sys
a = sys.stdin.readline().rstrip()

for i in range(int(a)):
    print("Case #"+str(i+1)+":",sum(map(int,sys.stdin.readline().rstrip().split())))