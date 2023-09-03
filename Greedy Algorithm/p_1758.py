"""
입력 : 첫째 줄 - 사람의 수 N
      이후 - 각 사람이 주려고 하는 팁
출력 : 받을 수 있는 최대 팁
"""

N = int(input())
tip = []
result = 0

for i in range(N):
    tip.append(int(input()))

tip.sort(reverse=True)

for j in range(N):
    if tip[j] - j < 0:
        continue
    else:
        result += (tip[j] - j)
print(result)
