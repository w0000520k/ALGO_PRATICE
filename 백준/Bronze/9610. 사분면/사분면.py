n = int(input())
D1 = 0
D2 = 0
D3 = 0
D4 = 0
axis = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        D1 = D1 + 1
    elif a < 0 and b > 0:
        D2 = D2 + 1
    elif a < 0 and b < 0:
        D3 = D3 + 1
    elif a > 0 and b < 0:
        D4 = D4 + 1
    elif a == 0 or b == 0:
        axis = axis + 1

print("Q1:", D1)
print("Q2:", D2)
print("Q3:", D3)
print("Q4:", D4)
print("AXIS:", axis)