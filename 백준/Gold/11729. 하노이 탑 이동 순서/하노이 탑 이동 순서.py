def hanoi(n, start, end, aux, moves):
    if n == 1:
        moves.append((start,end))
        return
    hanoi(n-1, start, aux, end, moves)
    moves.append((start, end))
    hanoi(n-1, aux, end, start, moves)

N = int(input())

moves=[]
hanoi(N, 1, 3, 2, moves)

print(len(moves))

for move in moves:
    print(f"{move[0]} {move[1]}")
