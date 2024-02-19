import sys
def ponix(n, a:list):
    stacks = [[0] for _ in range(4)]

    for i in a:
        isInserted = False
        for j in range(4):
            if stacks[j][-1] < i:
                stacks[j].append(i)
                isInserted=True
                break
        if not isInserted:
            return "NO"
    return "YES"
        
    

n,*a = map(int,sys.stdin.read().rsplit())

print(ponix(n,a))