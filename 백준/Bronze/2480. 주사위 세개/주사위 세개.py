a,b,c=map(int,input().split())

l=[a,b,c]

if a==b & b==c:
    s=10000+a*1000
if l.count(a)==3:
    s=10000+a*1000
elif l.count(b)==2:
    s=1000+b*100
elif l.count(c)==2:
    s=1000+c*100
else:
    l.sort(reverse=True)
    s=l[0]*100

print(s)