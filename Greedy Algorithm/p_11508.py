"""
입력 : 첫째 줄 - N (유제품 개수)
      이후 - C (유제품 가격)
출력 : N개의 유제품을 모두 살 떄 필요한 최소비용

[시간초과]
N = int(input())
arr = []
cost = 0

for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

for j in range(N):
    if (j + 1) % 3 == 0:    # 3의 배수가 아닐 경우 더하지만 않으면 됨 -> (j+1)%3!=0으로 수정
        continue
    else:
        cost += arr[j]

print(cost)
"""
from sys import stdin

N = int(stdin.readline())
arr = []
cost = 0

for i in range(N):
    arr.append(int(stdin.readline()))

arr.sort(reverse=True)

for j in range(N):
    if (j + 1) % 3 != 0:
        cost += arr[j]

print(cost)
