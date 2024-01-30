a,b,v=map(int,input().split())

c=(v-a)//(a-b)

d=(v-a)%(a-b)

if d == 0:
    print(c+1)
else:
    if d <= a:
        print(c+2)
