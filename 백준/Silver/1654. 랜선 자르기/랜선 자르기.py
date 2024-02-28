import sys

def bst_max_length(l, N):
    start, end = 1, max(l)
    
    while start <= end:
        mid = (start+end) // 2
        count = 0
        for i in l:
            count += i // mid
        if count >= N:
            start = mid + 1
        else:
            end = mid -1

    return end



K, N, *l = map(int,sys.stdin.read().rsplit())

print(bst_max_length(l, N))