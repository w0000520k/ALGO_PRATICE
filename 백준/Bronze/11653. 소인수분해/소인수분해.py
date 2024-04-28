N = int(input()) # 6
i = 2

while True:
    if N > i:
        if N % i == 0:
            print(i)
            N = N // i
        elif N % i != 0:
            i = i + 1
    elif N == i:
        print(i)
        break
    elif N < i:
        break