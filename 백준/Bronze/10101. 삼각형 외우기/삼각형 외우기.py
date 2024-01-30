l=list(map(int,open(0).read().split()))

if sum(l)==180:
    c=max(l)
    if l.count(c)==3:
        print("Equilateral")
    elif l.count(c)==2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")