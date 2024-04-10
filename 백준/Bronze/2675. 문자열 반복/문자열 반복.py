# 테스트 케이스의 개수 T를 입력받음
T = int(input())

# T만큼 반복
for _ in range(T):
    # 반복 횟수 R과 문자열 S를 입력받음
    R, S = input().split()
    R = int(R)  # R을 정수형으로 변환

    # 새 문자열 P를 초기화
    P = ''

    # 문자열 S의 각 문자를 R번 반복하여 P에 추가
    for char in S:
        P += char * R
    
    # 결과 문자열 P 출력
    print(P)