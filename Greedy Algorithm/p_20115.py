"""
입력 : 첫째 줄 - 자연수 N (에너지 드링크 수)
      이후 - x (에너지 드링크 양)
출력 : 최대로 만들 수 있는 에너지 드링크 양
"""

from sys import stdin

N = int(stdin.readline())
drink = list(map(int, stdin.readline().split()))
amount = 0

drink.sort(reverse=True)
amount += drink[0]

for i in range(1, N):
    amount += (drink[i] / 2)

# 20.0을 20으로 출력하기 위함 (if문 사용 x)
print('%g' % amount)

# if amount == int(amount):
#     print(int(amount))
# else:
#     print(amount)
