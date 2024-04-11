import sys

N = int(input())
numbers = list(map(int, input().split()))

if len(numbers) != N :
    sys.exit()

max = numbers[0]

min = numbers[0]

for i in numbers :
    if i > max :
        max = i

for i in numbers :
    if min > i :
        min = i

print(min, max)