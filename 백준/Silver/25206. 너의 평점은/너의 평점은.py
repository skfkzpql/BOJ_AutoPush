import sys

j=0
k=0
l = dict(zip(['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F'],[4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]))


ads = open(0).readlines()

for cc in ads:
    _,a,b = cc.split()
    if b != 'P':
        j += float(a)
        k += float(a)*l[b]
    
    if a == False:
        break

print(k/j)