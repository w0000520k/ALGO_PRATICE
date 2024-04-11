numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers :
    inputnum = int(input())
    if i == numbers[0] :
        max = inputnum
        countnum = 1
    elif i != numbers[0] :
        if inputnum > max :
            max = inputnum
            countnum = i
    
    i = i + 1

print(max)
print(countnum)