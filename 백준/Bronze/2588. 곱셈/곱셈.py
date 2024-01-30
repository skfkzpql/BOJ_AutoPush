a = int(input())
b = str(input())

for i in b[::-1]:
  print(a*int(i))

print(a*int(b))
