"""
입력 : 지우고 남은 수를 한 줄로 이어 붙인 수
출력 : 가능한 N중에 최솟값 출력
"""

from sys import stdin

S = stdin.readline().rstrip()

result = 0
current = 0

while True:
    result += 1
    for i in str(result):
        if S[current] == i:
            current += 1
            if current >= len(S):
                print(result)
                exit()