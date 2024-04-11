baskets_A = []

for _ in range(10) :
    i = int(input())
    j = i % 42

    if baskets_A.count(j) == 0 :
        baskets_A.append(j)

print(len(baskets_A))