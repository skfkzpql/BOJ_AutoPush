import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

graph = {i: [] for i in range(1, N+1)}

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

def dfs(v, k):
    visited = [False] * (N + 1)
    visited[v] = True
    count = 0
    stack = deque([(v, sys.maxsize)])

    while stack:
        v, usado = stack.pop()
        for next_v, next_usado in graph[v]:
            r = min(usado, next_usado)
            if r >= k and not visited[next_v]:
                count += 1
                stack.append((next_v, r))
                visited[next_v] = True

    return count


for _ in range(Q):
    k, v = map(int, input().split())
    print(dfs(v, k))
