l = [*map(int, open(0).read().rsplit())]
s = 0

for i in l:
    if i < 40:
        i = 40
    s += i
    
print(s // 5)