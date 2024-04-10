import sys

A, B = input().split()
A = int(A)
B = int(B)
if (-10000) <= A and B <= (10000) :
    if A > B :
        print(">")
    elif A < B :
        print("<")
    else :
        print("==")
else:
    sys.exit()