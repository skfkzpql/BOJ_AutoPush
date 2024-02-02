def solution(sides):
    sides=sorted(sides)
    answer = '21'[+(sides[2]<sum(sides[0:2]))]
    return int(answer)