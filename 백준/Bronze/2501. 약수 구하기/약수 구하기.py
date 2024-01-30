a,b=map(int,input().split())

j=0
for i in range(1,a+1):
    if a%i==0:
        j+=1
        if j==b:
            print(i)
            break
    if i==a:
        print(0)