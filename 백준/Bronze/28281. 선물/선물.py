a, b = map(int,input().split())
l = list(map(int,input().split()))
ll = []

for i in range(a-1):
    ll.append(sum(l[i:i+2]))

print(min(ll)*b)