l = [i if i != "/" else "//" for i in open(0).read().rsplit()]
idx = 0
ans = l[idx]
idx+=1
while True:
    if l[idx] == "=":
        break
    ans = str(eval(ans + ''.join(l[idx:idx+2])))
    idx += 2

print(ans)