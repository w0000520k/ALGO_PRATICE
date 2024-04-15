white_input = list(map(int, input().split()))
C = [0, 0, 0, 0, 0, 0]

if white_input[0] == 1:
    C[0] = 0
else :
    C[0] = 1 - white_input[0]

if white_input[1] == 1:
    C[1] = 0
else :
    C[1] = 1 - white_input[1]

if white_input[2] == 2:
    C[2] = 0
else :
    C[2] = 2 - white_input[2]

if white_input[3] == 2:
    C[3] = 0
else :
    C[3] = 2 - white_input[3]


if white_input[4] == 2:
    C[4] = 0
else :
    C[4] = 2 - white_input[4]

if white_input[5] == 8:
    C[5] = 0
else :
    C[5] = 8 - white_input[5]

print(' '.join(map(str, C)))