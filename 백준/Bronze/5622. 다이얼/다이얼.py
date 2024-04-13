import sys

N = input()
if (len(N) < 2) or (len(N) > 15) or (N.isupper() == False):
    sys.exit()

sum = 0

for i in range(len(N)) :
    if N[int(i)] == 'A' or N[int(i)] == 'B' or N[int(i)] == 'C' :
        sum = sum + 3
    elif N[int(i)] == 'D' or N[int(i)] == 'E' or N[int(i)] == 'F' :
        sum = sum + 4
    elif N[int(i)] == 'G' or N[int(i)] == 'H' or N[int(i)] == 'I' :
        sum = sum + 5
    elif N[int(i)] == 'J' or N[int(i)] == 'K' or N[int(i)] == 'L' :
        sum = sum + 6
    elif N[int(i)] == 'M' or N[int(i)] == 'N' or N[int(i)] == 'O' :
        sum = sum + 7
    elif N[int(i)] == 'P' or N[int(i)] == 'Q' or N[int(i)] == 'R' or N[int(i)] == 'S':
        sum = sum + 8
    elif N[int(i)] == 'T' or N[int(i)] == 'U' or N[int(i)] == 'V' :
        sum = sum + 9
    elif N[int(i)] == 'W' or N[int(i)] == 'X' or N[int(i)] == 'Y' or N[int(i)] == 'Z':
        sum = sum + 10


print(sum)