
A, B, C = map(int, input().split())

if A >= B and A >= C:
    if B >= C:
        print(B)
    else:
        print(C)
elif B >= C and B >= A:
    if C >= A:
        print(C)
    elif A >= C:
        print(A)
elif C >= A and C >= B:
    if A >= B:
        print(A)
    elif B >= A:
        print(B)