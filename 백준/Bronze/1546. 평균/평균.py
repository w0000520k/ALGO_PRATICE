import sys

N = int(input())
i = list(map(int, input().split()))
max = 0
sum = 0

if len(i) == N :
    for j in i :
        if j >= max :
            max = j

    for j in i :
        j = ((j/max)*100)
        sum = sum + j
    
    print(sum/N)

else :
    sys.exit()