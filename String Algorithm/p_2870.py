"""
입력 : 첫째 줄 - N (종이의 줄 개수)
      이후 - 각 줄의 내용
출력 : 비내림차순으로 \n으로 하나씩 출력
"""

from sys import stdin

N = int(stdin.readline())
result = []

for i in range(N):
    num = ""
    S = stdin.readline()
    for j in range(len(S)):
        if S[j].isdigit():
            num += S[j]
        else:
            if num != "":
                result.append(int(num))
                num = ""

result.sort()

for k in range(len(result)):
    print(result[k])
