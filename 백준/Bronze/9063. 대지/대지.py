a, *b = map(int,open(0).read().split())
c=b[0::2]
d=b[1::2]
print((max(c)-min(c))*(max(d)-min(d))*+(a>1))