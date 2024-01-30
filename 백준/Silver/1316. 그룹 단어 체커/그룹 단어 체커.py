a = int(input())
c = a
for i in range(a):
    b = input()
    for j in range(len(b)-1):
        if b[j] != b[j+1]:
            if b[j+1:].count(b[j]) != 0:
                c -= 1
                break

print(c)