a=input()
b=[-1]*26
for i in range(len(a)):
    c = b[ord(a[i])-97]
    if c == -1:
        b[ord(a[i])-97] = i
print(*b)