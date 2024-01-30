a=int(input())

b=0 #이전 넘버
c=1 #
i=0
s=1
while True:
    if a<=s:
        k=s-a
        break
    b=s
    c+=1
    s+=c
    i+=1
    
    
if i%2==1:
    print(c-k,'/',1+k,sep='')
else:
    print(1+k,'/',c-k,sep='')