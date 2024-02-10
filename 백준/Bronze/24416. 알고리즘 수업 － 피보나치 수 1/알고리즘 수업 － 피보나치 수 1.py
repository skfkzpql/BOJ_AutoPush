def fibonacci_dp(n):
    # 기존 재귀 함수에서 사용한 리스트와 동일한 이름을 사용합니다.
    fib_values = [0] * (n + 1)
    return fibonacci_recursive(n, fib_values)

def fibonacci_recursive(n, fib_values):
    if n <= 2:
        return 1
    # 이미 계산한 값이 있다면 해당 값을 반환합니다.
    if fib_values[n] != 0:
        return fib_values[n]
    # 계산하지 않은 경우 계산하여 저장합니다.
    fib_values[n] = fibonacci_recursive(n - 1, fib_values) + fibonacci_recursive(n - 2, fib_values)
    return fib_values[n]

n = int(input())

# 동적 프로그래밍을 사용하여 피보나치 수 계산
fib_dp = fibonacci_dp(n)

# 결과 출력
print(fib_dp, n-2)
