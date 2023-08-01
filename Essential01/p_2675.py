"""
입력 : 첫째 줄 - 테스트 케이스 T, 이후 - 반복 횟수 R (공백) 문자열 S
출력 : 문자역 * 반복횟수
"""

T = int(input())
list = []

for i in range(T):
    R, S = map(str, input().split())

    for j in range(len(S)):
        print(S[j] * int(R), end='')    # 줄바꿈 없이 이어서 출력하기 위해 end사용

    print() # 줄바꿈을 하기 위함
