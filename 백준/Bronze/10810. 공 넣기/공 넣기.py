N, M = map(int, input().split())

baskets = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for b in range(i-1, j):  
        baskets[b] = k


print(' '.join(map(str, baskets)))