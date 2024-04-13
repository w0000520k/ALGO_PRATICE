A, B = map(str, input().split())
A = A[2:] + A[1:2] + A[:1]
B = B[2:] + B[1:2] + B[:1]

A = int(A)
B = int(B)

if A > B :
    print(A)
else :
    print(B)