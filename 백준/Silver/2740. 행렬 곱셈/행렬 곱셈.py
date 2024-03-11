def matrix_multiplication_optimized(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for k in range(len(B)):
            for j in range(len(B[0])):
                result[i][j] += A[i][k] * B[k][j]

    return result

f = open(0)
n, m = map(int, f.readline().rsplit())
A = [list(map(int, f.readline().rsplit())) for _ in range(n)]
k, _ = map(int, f.readline().rsplit())
B = [list(map(int, f.readline().rsplit())) for _ in range(k)]


result_matrix = matrix_multiplication_optimized(A, B)

for row in result_matrix:
    print(*row)
