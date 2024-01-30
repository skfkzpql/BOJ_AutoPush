file = open(0)
line = file.readline()
while line:
    a,b=line.split()
    print(int(a)+int(b))
    line = file.readline()
file.close()