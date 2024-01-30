a=int(input())
s=0
i=0
while True:
    if (a==5) or (a==3):
        i+=1
        break
    elif a<3:
        s=-1
        i=0
    if a%5==0:
        s=a//5
        break
    else:
        a-=3
        i+=1

print(s+i)