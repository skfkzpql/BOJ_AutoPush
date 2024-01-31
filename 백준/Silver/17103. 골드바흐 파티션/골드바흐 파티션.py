# 에라토스테네스의 체를 사용하여 소수 리스트를 생성하는 함수
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    return primes

# 입력 처리 및 출력
T = int(input())
max_N = 1000000  # 주어진 범위의 최대값
primes = sieve_of_eratosthenes(max_N)

for _ in range(T):
    N = int(input())
    count = 0
    
    # 짝수 N에 대한 골드바흐 파티션 수 계산
    i = 0
    j = len(primes) - 1
    while i <= j:
        if primes[i] + primes[j] == N:
            count += 1
            i += 1
            j -= 1
        elif primes[i] + primes[j] < N:
            i += 1
        else:
            j -= 1
    
    print(count)
