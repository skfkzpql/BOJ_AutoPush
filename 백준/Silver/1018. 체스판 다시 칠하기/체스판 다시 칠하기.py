a,b,*l=open(0).read().split()
a=int(a)
b=int(b)
start_B=0
start_W=0
zx=[]
for i in range(a-7):
    for j in range(b-7):
        start_w_B=0
        start_w_W=0
        for k in range(0,8):
            if k%2==0:
                start_w_B+=l[k+i][j:j+7:2].count('B')
                start_w_B+=l[k+i][j+1:j+8:2].count('W')
                start_w_W+=l[k+i][j:j+7:2].count('W')
                start_w_W+=l[k+i][j+1:j+8:2].count('B')
            else:
                start_w_B+=l[k+i][j:j+7:2].count('W')
                start_w_B+=l[k+i][j+1:j+8:2].count('B')
                start_w_W+=l[k+i][j:j+7:2].count('B')
                start_w_W+=l[k+i][j+1:j+8:2].count('W')
            zx.append(start_w_B)
            zx.append(start_w_W)
          



print(64-max(zx))