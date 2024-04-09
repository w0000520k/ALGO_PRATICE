import sys

input_text = input()
check_alpha = "abcdefghijklmnopqrstuvwxyz"

ans = ""

if input_text.islower() and len(input_text) <= 100 :
    for i in check_alpha:
        if not input_text.find(i) < 0:
            if input_text[0] == i:
                ans = ans + " 0"
            elif input_text[1] == i:
                ans = ans + " 1"
            else :
                ans = ans + " " + str(input_text.find(i))
        else :
            ans = ans + " -1"

print(ans.lstrip())
