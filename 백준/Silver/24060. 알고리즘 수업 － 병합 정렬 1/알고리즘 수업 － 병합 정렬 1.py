def merge(A, p, q, r, K, save_count):
    i, j, t = p, q + 1, 0
    tmp = [0] * (r - p + 1)
    global merge_count
    global kth_value
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1
        merge_count += 1
        if merge_count == K:
            kth_value = tmp[t-1]
    
    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1
        merge_count += 1
        if merge_count == K:
            kth_value = tmp[t-1]
    
    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1
        merge_count += 1
        if merge_count == K:
            kth_value = tmp[t-1]
    
    A[p:r+1] = tmp
    
def merge_sort(A, p, r, K, save_count):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, K, save_count)
        merge_sort(A, q + 1, r, K, save_count)
        merge(A, p, q, r, K, save_count)

N, K = map(int, input().split())  # 배열의 크기 N, 저장 횟수 K
A = list(map(int, input().split()))  # 배열 A

merge_count = 0  # 병합 과정에서의 저장 횟수
kth_value = -1  # K 번째 저장되는 값 (기본값 -1)

merge_sort(A, 0, N-1, K, merge_count)

print(kth_value)
