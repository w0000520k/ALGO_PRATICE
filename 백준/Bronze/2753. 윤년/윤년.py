import sys

A = input()
A = int(A)

if 1 <= A <= 4000:
    if A % 4 == 0 and (A % 100 != 0 or A % 400 == 0):
        print("1")
    else :
        print("0")
else :
    sys.exit()