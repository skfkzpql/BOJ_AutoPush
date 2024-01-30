while True:
    a = int(input())
    if a == -1:
        break
    l=[]
    for i in range(1,a+1):
        if a%i == 0:
            l.append(i)
    
    print(a,end=' ')
    if sum(l[0:-1])==a:
        print('=',end=' ')
        for j in l[0:-1]:
            if j==l[-2]:
                print(j)
            else:
                print(j,"+ ",end='')
    else:
        print("is NOT perfect.")