import sys

def order(c:str):
    l, r = d[c][0], d[c][1]
    preOrderList.append(c)
    if l != '.':
        order(l)
    inOrderList.append(c)
    if r != '.':
        order(r)
    postOrderList.append(c)

n = int(sys.stdin.readline())

d = {}
preOrderList = []
inOrderList = []
postOrderList = []

for i in sys.stdin:
    p, l, r = i.split()
    d[p] = [l,r]

order('A')
print(*preOrderList,sep="")
print(*inOrderList,sep="")
print(*postOrderList,sep="")