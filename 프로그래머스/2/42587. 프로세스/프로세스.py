from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(enumerate(priorities))

    e = []

    while len(q) != 1:
        (i, j) = q.popleft()
        e.append((i, j))
        
        if j < max([t[1] for t in q]):
            q.append(e.pop())
            
    e.append(q.pop())
    
    return [t[0] for t in e].index(location) + 1