l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
c = len(a)
for i in l:
    k = a.count(i)
    if k > 0:
        c -= k

print(c)