def solution(s):
    d={}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    l = [c for c, i in d.items() if i == 1]

    return ''.join(sorted(l))