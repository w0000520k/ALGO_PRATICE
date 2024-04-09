import sys

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if 1 <= A <= (10 ** 12) and 1 <= B <= (10 ** 12) and 1 <= C <= (10 ** 12) :
    print(A+B+C)
else:
    sys.exit()