x = int(input())
l = [1] * (x + 1)
l[1] = 0
if x > 3:
    for i in range(4, x + 1):
        a=b=float('inf')
        if i%3==0:
            a = l[i//3]
        if i%2==0:
            b = l[i//2]
        c = l[i-1]
        l[i]+=min(a,b,c)
print(l[x])