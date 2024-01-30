a, b = open(0).read().split()
s = 0
for i, j in enumerate(a[::-1]):
    if j.isalpha():
        c=ord(j)-55
    else:
        c=int(j)
    s+=(int(b)**i)*c
print(s)