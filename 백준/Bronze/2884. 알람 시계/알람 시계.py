a,b=map(int,input().split())
if b>=45:
    m = b-45
    h = a
else:
    m = b+15
    if a==0:
        h = 23
    else:
        h = a-1

print(h,m)