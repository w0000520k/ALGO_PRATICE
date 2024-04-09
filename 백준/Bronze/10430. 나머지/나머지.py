import sys

A, B, C = input().split()
A = int(A)
if not 2 <= A <= 10000 :
    sys.exit()
B = int(B)
if not 2 <= B <= 10000 :
    sys.exit()
C = int(C)
if not 2 <= C <= 10000 :
    sys.exit()

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
