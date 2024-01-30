a= int(input())
b= int(input())
l=[]

for i in range(a,b+1):
    if i != 1:
        if i < 4:
            l.append(i)
        elif i % 2 != 0:
            for j in range(3,i+1):
                if i == j:
                    l.append(i)
                elif i%j==0:
                    break

if len(l)==0:
    print("-1")
else:
    print(sum(l),l[0],sep='\n')