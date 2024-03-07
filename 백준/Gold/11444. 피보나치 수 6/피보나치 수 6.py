n = int(input())
MOD = 10 ** 9 + 7

matrix = [[1, 1], [1, 0]]


def matrix_multiplication(m1, m2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + m1[i][k] * m2[k][j]) % MOD
    return result


exp = n
answer = [[1, 0], [0, 1]]  # 단위 행렬로 초기화

while exp > 0:
    if exp % 2:
        answer = matrix_multiplication(answer, matrix)
    matrix = matrix_multiplication(matrix, matrix)
    exp //= 2

print(answer[1][0])
