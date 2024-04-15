S = input()
sum = 0
j = 0

croa_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
change_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in croa_alpha:
    sum = sum + S.count(i)
    S = S.replace(i, change_alpha[j])
    j = j + 1

print(len(S))