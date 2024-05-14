N = int(input())
numbers = list(map(int, input().split()))
C = 0

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for i in numbers:
    if is_prime(i):
        C += 1

print(C)