file = open(0)
total = file.readline()
a = file.readline()
cal = 0
for i in range(int(a)):
    b,c = map(int,file.readline().split())
    cal += b*c

if cal == int(total):
    print("Yes")
else:
    print("No")
