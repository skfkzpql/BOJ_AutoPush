from collections import defaultdict

f = open(0)
n = int(f.readline())
edges = [list(map(int, f.readline().rsplit())) for _ in range(n - 1)]

graph = defaultdict(list)
parents = [0] * (n+1)

for edge in edges:
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)

stack = [1]
visited = [False] * (n+1)

while stack:
    node = stack.pop()
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            parents[neighbor] = node
            stack.append(neighbor)

print(*parents[2:],sep='\n')