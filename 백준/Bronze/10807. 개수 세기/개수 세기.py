import sys

countnum = int(input())
numbers = list(map(int, input().split()))
if len(numbers) > countnum :
    sys.exit()
v = int(input())

print(numbers.count(v))