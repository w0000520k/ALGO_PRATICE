X = int(input())
N = int(input())
sum = 0

for i in range(N) :
    a, b = map(int, input().split())
    sum = sum + (a * b)

if X == sum :
    print("Yes")
else :
    print("No")