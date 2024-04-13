import sys

N = int(input())
N_num = input()
if len(N_num) != N :
    sys.exit()

sum = 0

for i in range(N) :
    sum = sum + int(N_num[i])
    i = i + 1

print(sum)