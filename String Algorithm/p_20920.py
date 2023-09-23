"""
입력 : 첫째 줄 - N (공백) M
      이후 - 영단어 (N만큼)
출력 : 단어장의 앞에 위치한 단어부터 한 줄에 한 단어씩 순서대로 출력
"""

from sys import stdin

N, M = map(int, stdin.readline().split())
dic = {}

for i in range(N):
    word = stdin.readline().rstrip()

    if word in dic:
        dic[word] += 1
    else:
        if len(word) >= M:
            dic[word] = 1

result = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for j in range(len(result)):
    print(result[j][0])
