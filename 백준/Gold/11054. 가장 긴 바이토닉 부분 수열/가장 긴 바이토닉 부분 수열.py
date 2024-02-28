N, *A = map(int, open(0).read().split())

dp_inc = [1] * N
dp_dec = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

        if A[N - 1 - i] > A[N - 1 - j]:
            dp_dec[N - 1 - i] = max(dp_dec[N - 1 - i], dp_dec[N - 1 - j] + 1)

max_length = max([dp_inc[i] + dp_dec[i] - 1 for i in range(N)])

print(max_length)
