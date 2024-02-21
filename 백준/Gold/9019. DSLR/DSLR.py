from collections import deque

MOD = 10000

def bfs(a, b):
    visited = [0] * 10000
    queue = deque([("", a)])

    visited[a] = 1
    while queue:
        command, n = queue.popleft()

        if n == b:
            print(command)
            return

        m = (2 * n) % MOD
        if not visited[m]:
            visited[m] = 1
            queue.append((command + "D", m))

        m = 9999 if n == 0 else n - 1
        if not visited[m]:
            visited[m] = 1
            queue.append((command + "S", m))

        m = (n % 1000) * 10 + n // 1000
        if not visited[m]:
            visited[m] = 1
            queue.append((command + "L", m))

        m = (n % 10) * 1000 + n // 10
        if not visited[m]:
            visited[m] = 1
            queue.append((command + "R", m))


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    bfs(A, B)
