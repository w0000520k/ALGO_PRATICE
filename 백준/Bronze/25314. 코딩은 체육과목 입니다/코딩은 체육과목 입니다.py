N = int(input())
N = N // 4
M = ""

for i in range(N):
    M = M + "long "
    i = i + 1

if N >= 1 :
    print(M + "int")
else :
    print("int")