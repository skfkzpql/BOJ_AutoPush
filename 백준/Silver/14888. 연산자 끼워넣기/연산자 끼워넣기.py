import sys

def operate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if a < 0:
            return -(-a // b)
        else:
            return a // b
        
def dfs(idx, cur_result):
    global max_result, min_result, numbers, operators_count

    if idx == N:
        max_result = max(max_result, cur_result)
        min_result = min(min_result, cur_result)
        return
    
    for i in range(4):
        if operators_count[i] > 0:
            operators_count[i] -= 1
            dfs (idx + 1, operate(cur_result, numbers[idx], operators[i]))
            operators_count[i] += 1



# 입력
N = int(input())
numbers = list(map(int, input().split()))
operators_count = list(map(int, input().split()))  # [덧셈 개수, 뺄셈 개수, 곱셈 개수, 나눗셈 개수]
operators = ['+', '-', '*', '/']

# 최댓값과 최솟값 초기화
max_result = -sys.maxsize
min_result = sys.maxsize

# 탐색 시작
dfs(1, numbers[0])

# 출력
print(max_result)
print(min_result)