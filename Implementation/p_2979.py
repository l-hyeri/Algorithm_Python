"""
입력 : 첫째 줄 - A, B, C (주차 요금)
      이후 - 도착 시간 (공백) 떠난 시간
출력 : 주차 요금 출력
"""

from sys import stdin

A, B, C = map(int, stdin.readline().split())
arr = [0] * 101
cost = 0

for i in range(3):
    start, end = map(int, stdin.readline().split())

    for j in range(start, end):
        arr[j] += 1

for j in arr:
    if j == 1:
        cost += A

    elif j == 2:
        cost += 2 * B

    elif j == 3:
        cost += 3 * C

    else:
        continue

print(cost)
