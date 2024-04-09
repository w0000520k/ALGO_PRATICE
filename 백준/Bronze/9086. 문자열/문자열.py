import sys
T = input()
T = int(T)
if not 1 <= T <= 10 and T.isupper():
    sys.exit()
    
count = 0
a = range(10)

for i in a:
    if not count == T:
        A = input()
        if A.count(" ") == 0:
            print(A[0] + A[-1])
        else :
            sys.exit()
    else:
        sys.exit()
    count = count + i