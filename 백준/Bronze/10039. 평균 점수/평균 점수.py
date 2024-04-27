sum = 0

for _ in range(5):
    a = int(input())
    if a <= 40:
        a = 40
    sum = sum + a

print(int(sum/5))