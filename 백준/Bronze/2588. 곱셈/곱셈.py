import sys

A = input()
B = input()
if len(A) < 4 and len(B) < 4 :
    print(int(A)*int(B[2]))
    print(int(A)*int(B[1]))
    print(int(A)*int(B[0]))
    print(int(A)*int(B))
else :
    sys.exit()