def solution(friends, gifts):
    d=dict((b,a) for a,b in enumerate(friends,0))
    l = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    r = dict(zip(friends,[0 for _ in range(len(friends))]))

    lcopy =[0 for _ in range(len(friends))]

    for i in gifts:
        i, j = i.split()
        r[i] += 1
        r[j] -= 1
        l[d[i]][d[j]] += 1


    for i in range(len(friends)):
        for j in range(len(friends)):
            if i < j:
                k = l[i][j] - l[j][i]
                if k == 0:
                    if r[friends[i]] > r[friends[j]]:
                        lcopy[i] += 1
                    elif r[friends[i]] < r[friends[j]]:
                        lcopy[j] += 1
                elif k > 0:
                    lcopy[i] += 1
                elif k < 0:
                    lcopy[j] += 1

    answer = max(lcopy)
    return answer