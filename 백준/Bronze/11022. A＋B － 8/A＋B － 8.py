import sys

T = int(input())

for i in range(1, T+1) :
    a, b = map(int, sys.stdin.readline().strip().split())
    print("Case #%d: %d + %d = %d" % (i , a, b, (a + b)))
    i = i + 1