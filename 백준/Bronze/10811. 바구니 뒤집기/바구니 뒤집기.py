import sys

N, M = map(int, input().split())
if 1 <= N <= 100 :
    N = [i for i in range(1, N+1)]
else :
    sys.exit()

for _ in range(M) :
    i, j = map(int, input().split())
    part_reversed = N[i-1:j][::-1]
    N = N[:i-1] + part_reversed + N[j:]

print(' '.join(map(str, N)))