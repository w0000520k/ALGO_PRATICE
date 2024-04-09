import sys

text = input()
if len(text) > 1000:
    sys.exit()

if not text.isalpha() :
    sys.exit()

number = input()
number_int = int(number)

if number_int > len(text) :
    sys.exit()
else:
    print(text[number_int - 1])