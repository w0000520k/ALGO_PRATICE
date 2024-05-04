def find_floor(N):
    max_num = 0
    i = 0
    pre = 0
    
    while max_num < N:
        if i == 0:
            max_num += 1  
        else:
            max_num += 6 * i  
            
        i += 1

        if pre < N <= max_num:
            return i

        pre = max_num

N = int(input())
floor = find_floor(N)
print(floor)