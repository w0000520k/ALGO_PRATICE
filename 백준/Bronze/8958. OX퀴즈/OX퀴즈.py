T = int(input())
count = 0
sum = 0
j = 0

for _ in range(T):
    A = input()
    for i in A:
        if j != len(A):
            if i == 'O':
                count = count + 1
                sum = sum + count
            else:
                count = 0

    print(sum)
    j = 0
    count = 0
    sum = 0