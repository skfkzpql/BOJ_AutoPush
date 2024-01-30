a=input()
b=9*len(a)
a=int(a)
d=0
for i in range(a-b,a):
    if i>0:
        c=[int(j) for j in str(i)]
        if sum(c)+i == a:
            d=i
            break


print(d)