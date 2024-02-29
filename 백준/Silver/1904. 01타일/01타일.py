n = int(input())

l = [0, 1, 2]
answer = l[n%3]
for i in range(3, n + 1):
    l[i % 3] = ((l[(i + 1) % 3] + l[(i + 2) % 3]) % 15746)
    answer = l[i % 3]

print(answer)
