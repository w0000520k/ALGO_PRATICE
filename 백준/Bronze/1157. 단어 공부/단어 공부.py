import sys
from collections import Counter

# 입력받은 문자열을 모두 대문자로 변환
input_str = sys.stdin.read().strip().upper()

# 문자의 빈도수를 계산
counter = Counter(input_str)

# 가장 많이 사용된 알파벳의 빈도수 구하기
max_count = max(counter.values())

# 가장 많이 사용된 알파벳이 여러 개인지 확인
if list(counter.values()).count(max_count) > 1:
    print('?')
else:
    # 가장 빈도수가 높은 알파벳 출력
    for char, count in counter.items():
        if count == max_count:
            print(char)
            break