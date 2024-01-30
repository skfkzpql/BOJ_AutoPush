l = [0 for i in range(30)]
for i in range(0,28):
    a = int(input())
    l[a-1]=1

for i in range(len(l)):
    if l[i] == 0:
        print(i+1)