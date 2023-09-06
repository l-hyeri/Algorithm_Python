"""
입력 : 자연수 N
출력 : 가장 작은 생성자 출력 (생성자가 없을 경우 0 출력)
"""

from sys import stdin

N = int(stdin.readline())

for i in range(1, N + 1):
    temp, sum = i, i

    while temp != 0:
        sum += (temp % 10)
        temp //= 10

    if N == sum:
        print(i)
        break

    if N == i:
        print(0)
        break
