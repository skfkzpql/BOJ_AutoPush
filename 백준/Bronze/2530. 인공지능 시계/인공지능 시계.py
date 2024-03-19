h,m,s,t = map(int, open(0).read().rsplit())

s += t
if s > 59:
    ad = s // 60
    s %= 60
    m += ad
    if m > 59:
        ad = m // 60
        m %= 60
        h += ad
        h %= 24
print(h,m,s)