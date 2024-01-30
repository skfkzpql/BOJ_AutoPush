import math

# 입력 받기
n = int(input())
values = [list(map(int, input().split())) for _ in range(n)]

# 최소공배수 계산 및 출력
for j, k in values:
    print(math.lcm(j,k))