"""
입력 : 첫째 줄 - 단어의 개수
      이후 - 단어 줄어짐 (모두 대문자)
출력 : 첫번째 단어와 비슷한 단어가 몇개인지 출력
"""

from sys import stdin
N = int(input())
target = list(input()) # 비교 대상 단어(첫 단어)
answer = 0

for _ in range(N-1):
    compare = target[:]
    word = input() # 새로운 단어
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)

