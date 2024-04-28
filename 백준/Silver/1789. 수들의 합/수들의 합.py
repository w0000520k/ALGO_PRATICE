S = int(input())
i = 1
j = 0

while True:
    S = S - i
    if S < 0:
        break
    else:
        i = i + 1
        j = j + 1

print(j)