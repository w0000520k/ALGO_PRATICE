import sys

H, M = map(int, input().split())

if M < 45 :
    H = H - 1
    M = M - 45 + 60
else :
    M = M - 45

if H < 0 :
    H = 23

print(H, M)