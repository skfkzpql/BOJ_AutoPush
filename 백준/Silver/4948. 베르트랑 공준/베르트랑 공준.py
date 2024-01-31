def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

while True:
    a = int(input())
    if a == 0:
        break
    count = 0
    for i in range(a + 1, 2 * a + 1):
        if is_prime(i):
            count += 1
    print(count)