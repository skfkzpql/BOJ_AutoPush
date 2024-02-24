num_elements = int(input())
input_sequence = list(map(int, input().split()))

dp_table = [1] * num_elements

for i in range(1, num_elements):
    for j in range(i):
        if input_sequence[i] > input_sequence[j]:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)

print(max(dp_table))
