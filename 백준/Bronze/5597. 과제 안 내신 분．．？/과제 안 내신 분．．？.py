N = 30
S = [i for i in range(1, N+1)]

for _ in range(28) :
    i = int(input())
    j = S.index(i)
    del S[j]

print(S[0])
print(S[1])