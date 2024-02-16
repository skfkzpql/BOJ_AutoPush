def solution(s):
    a = 0
    for i in s:
        if i == '(':
            a += 1
        elif a == 0:
            return False
        else:
            a -= 1

    return a == 0