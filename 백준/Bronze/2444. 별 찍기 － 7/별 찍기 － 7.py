a=int(input())

for i in range(1,2*a):
    b = 2*(a-abs(a-i))-1
    c = (2*a-1-b)//2
    print(' '*c,'*'*b,sep='')