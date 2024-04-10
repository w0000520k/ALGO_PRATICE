A, B, C = map(int, input().split())

if A == B == C :
    H = 10000 + A * 1000
elif A == B :
    H = 1000 + A * 100
elif B == C :
    H = 1000 + B * 100
elif A == C :
    H = 1000 + A * 100
else :
    if A > B and A > C :
        H = A * 100
    elif B > A and B > C :
        H = B * 100
    else :
        H = C * 100

print(H)