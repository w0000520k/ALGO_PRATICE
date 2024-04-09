import sys

a, b = input().split()
a = int(a)
b = int(b)

if 1 <= a and 0 < b <= 10000 :
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)

else :
    sys.exit()
