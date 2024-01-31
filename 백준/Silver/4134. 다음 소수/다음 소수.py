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

# 테스트 케이스 개수 입력
t = int(input())

# 각 테스트 케이스에 대한 처리
for _ in range(t):
    n = int(input())
    
    # n보다 크거나 같은 소수를 찾을 때까지 n을 증가시키며 소수 판별
    while not is_prime(n):
        n += 1
    
    print(n)