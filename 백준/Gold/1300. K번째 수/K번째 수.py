def find_kth_number(n, k):
    start, end = 1, k  # 이진 탐색을 위한 시작과 끝 값 설정

    while start <= end:
        mid = (start + end) // 2
        count = 0

        # mid보다 작거나 같은 값을 가지는 원소의 개수를 세기
        for i in range(1, n + 1):
            count += min(mid // i, n)

        # count가 k보다 작다면 mid 값 증가, 크다면 end 값 감소
        if count < k:
            start = mid + 1
        else:
            end = mid - 1

    return start

# 입력 받기
n = int(input())
k = int(input())

# 결과 출력
result = find_kth_number(n, k)
print(result)
