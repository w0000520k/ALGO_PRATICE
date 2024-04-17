def is_group_word(word):
    seen = {}
    last_char = ''
    for char in word:
        if char in seen and char != last_char:
            return False
        seen[char] = True
        last_char = char
    return True

N = int(input())
group_word_count = 0

for _ in range(N):
    word = input()
    if is_group_word(word):
        group_word_count += 1

print(group_word_count)