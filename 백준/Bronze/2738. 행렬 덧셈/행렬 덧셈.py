N, M = map(int, input().split())

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

C = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    C.append(row)

for row in C:
    print(' '.join(map(str, row)))