def solution(progresses, speeds):
    done = []

    for i in range(len(progresses)):
        a = progresses[i]
        b = speeds[i]
        c = (100 - a) // b + ((100-a)%b > 0)
        done.append(c)

    result = []

    prevDone = 0
    for i in range(len(done)):
        if result == []:
            result.append(1)
            prevDone = done[0]
        elif done[i] > prevDone:
            result.append(1)
            prevDone = done[i]
        else:
            result[-1] += 1
    return result