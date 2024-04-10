import sys

A = input()
A = int(A)

if not (((-1000) <= A <= 1000) and A != 0) :
    sys.exit()

B = input()
B = int(B)

if not (((-1000) <= B <= 1000) and B != 0) :
    sys.exit()

if A < 0 :
    if B < 0 :
        print("3")
    else :
        print("2")
else :
    if B < 0 :
        print("4")
    else :
        print("1")
