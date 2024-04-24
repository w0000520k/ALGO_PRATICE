A, B, C = map(int, input().split())
D = int(input())

D_H = D // 3600
D_M = (D % 3600) // 60
D_S = D - (D_H * 3600) - (60 * D_M)

sum_S = C + D_S
sum_M = B + D_M
sum_H = A + D_H

if sum_S >= 60:
    s_count = sum_S // 60
    sum_S = sum_S % 60
    sum_M = sum_M + s_count

if sum_M >= 60:
    m_count = sum_M // 60
    sum_M = sum_M % 60
    sum_H = sum_H + m_count

if sum_H >= 24:
    sum_H = sum_H % 24

print(sum_H, sum_M, sum_S)
