a, b = map(int, input().split())

MOD = 1000000007


# 분할 정복을 이용한 거듭제곱 구현
def power(base, exp):
    result = 1
    base = base % MOD
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % MOD
        base = (base * base) % MOD
        exp //= 2
    return result


# 모듈로 곱셈 역원 구현
def mod_inverse(num):
    return power(num, MOD - 2)


# 이항 계수 구현
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    numerator = 1
    denominator = 1
    for i in range(1, min(k, n - k) + 1):
        numerator = (numerator * (n - i + 1)) % MOD
        denominator = (denominator * i) % MOD
    return (numerator * mod_inverse(denominator)) % MOD


print(binomial_coefficient(a, b))
