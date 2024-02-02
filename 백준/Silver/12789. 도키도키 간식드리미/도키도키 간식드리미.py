n = int(input())
line = list(map(int,input().split()))
line.reverse()
space = []
next_num = 1

while next_num != n:
    if len(line) > 0:
        a = line[-1]
    else:
        a = 0
    if a == next_num:
        next_num += 1
        line.pop()
    else:
        if len(space) == 0:
            space.append(line.pop())
        elif len(space) > 0:
            if space[-1] == next_num:
                next_num += 1
                space.pop()
            else:
                space.append(line.pop())
                if space[-1] > space[-2]:
                    break
            

if next_num == n:
    print("Nice")
else:
    print("Sad")