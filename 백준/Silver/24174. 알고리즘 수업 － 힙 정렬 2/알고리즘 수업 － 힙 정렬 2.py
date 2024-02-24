def heap_sort(arr):
    global cnt
    n = len(arr) - 1
    build_min_heap(arr, n)
    for i in range(n, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]  # Swap elements
        if (i != 1):
            cnt += 1
        heapify(arr, 1, i - 1)

def build_min_heap(arr, n):
    for i in range(n // 2, 0, -1):
        heapify(arr, i, n)


def heapify(arr, k, n):
    global cnt, K, result
    if cnt == K:
        result = arr[1:].copy()
        
    left = 2 * k
    right = 2 * k + 1
    if right <= n:
        if arr[left] < arr[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return

    if arr[smaller] < arr[k]:
        arr[k], arr[smaller] = arr[smaller], arr[k]
        if k != smaller:
            cnt+=1
 
        
        heapify(arr, smaller, n)

N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0,0)
cnt = 0

result=[]
heap_sort(arr)

if len(result) > 0:
    print(*result)
else:
    print(-1)
