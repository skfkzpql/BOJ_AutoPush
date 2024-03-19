l = open(0).readlines()[:-1]
for i in l:
    a, b = map(int, i.rsplit())
    if a > b:
        print("Yes")
    else:
        print("No")