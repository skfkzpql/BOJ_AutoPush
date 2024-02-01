t = int(input())

for i in range(t):
    b=input()
    r=len(b)
    c=0
    if r % 2 == 1 or b[0] == ')' or b[-1] == '(':
        print("NO")
    else:
        for j in b:
            if j=='(':
                c+=1
            else:
                c-=1
                if c < 0:
                    break
        if c == 0:
            print("YES")
        else:
            print("NO")