import sys

N, X = map(int, input().split())
numbers = list(map(int, input().split()))

numbers = [i for i in numbers if i < X]

# numbers.sort()
print(' '.join(map(str, numbers)))