def draw_stars(n):
    if n == 1:
        return ['*']

    Stars = draw_stars(n // 3)
    L = []

    for S in Stars:
        L.append(S * 3)
    for S in Stars:
        L.append(S + ' ' * (n // 3) + S)
    for S in Stars:
        L.append(S * 3)

    return L

N = int(input())
print('\n'.join(draw_stars(N)))
