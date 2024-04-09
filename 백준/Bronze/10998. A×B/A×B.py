import sys

a, b = input().split()
a = int(a)
b = int(b)

if 0 < a and b < 10 :
    print(a * b)
else :
    sys.exit()
