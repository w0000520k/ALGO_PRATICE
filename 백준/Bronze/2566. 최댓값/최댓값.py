row_counter = 1
max_vertical_index = 1

max_number = 0
gar = 0

for j in range(9):
    row = list(map(int, input().split()))
    for i in row:
        if i >= max_number:
            max_number = i
            gar = row.index(i) + 1
            max_vertical_index = row_counter

    row_counter += 1

print(max_number)
print(max_vertical_index, gar)