import sys

S = input()

if S.islower() == True:
    if len(S)%2 == 0:
        A = S[:len(S)//2]
        B = S[len(S)//2:][::-1]
        if A == B:
            print("1")
        else:
            print("0")
    else:
        A = S[:len(S)//2]
        B = S[(len(S)//2)+1:][::-1]
        if A == B:
            print("1")
        else:
            print("0")
else:
    sys.exit()