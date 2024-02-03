import sys
N = int(sys.stdin.readline().rstrip())

s = set()
after_ch = 0
for i in range(N):
    a = list(map(str,sys.stdin.readline().rsplit()))
    
    if 'ChongChong' in a:
        s.add(a[0])
        s.add(a[1])
    
    if a[0] in s or a[1] in s:
        s.add(a[0])
        s.add(a[1])

print(len(s))