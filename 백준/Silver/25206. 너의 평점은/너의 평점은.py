sum = 0
count = 0
J = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}

for _ in range(20):
    A, B, C = input().split()
    N = float(B)

    if C == 'P':
        continue
    else:
        sum = sum + (N * J[C])
        count = count + N

ans = sum/count
print("%.6f" % ans)
