import math

# 소수 판별 함수
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# 입력 받기
m, n = map(int, input().split())

# m보다 크고 n보다 작은 소수를 찾아 출력
for i in range(m, n + 1):
    if is_prime(i):
        print(i)