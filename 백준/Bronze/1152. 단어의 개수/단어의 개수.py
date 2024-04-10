import sys

S = input()

def contains_digit(s):
    for char in s:
        if char.isdigit():
            return True
    return False

if contains_digit(S) == False :
    if len(S) <= 1000000 :
        if S[0] == " " and S[-1] == " ":
            print(S.count(" ") - 1)
        elif S[0] == " " :
            print(S.count(" "))
        elif S[-1] == " " :
            print(S.count(" "))
        else:
            print(S.count(" ") + 1 )
    else:
        sys.exit()
else :
    sys.exit()