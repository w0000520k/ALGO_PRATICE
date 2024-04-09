import sys

S = input()
if S.islower() and len(S) <= 50 :
    print(S + "??!")
else :
    sys.exit()