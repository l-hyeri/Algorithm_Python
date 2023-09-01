"""
입력 : 첫째 줄 - N,M (N : 스크린 크기, M : 바구니 크기)
      둘째 줄 - 떨어지는 사과의 개수 J (1이상 20이하)
      이후 - J개의 줄에 사과가 떨어지는 위치
출력 : 모든 사과를 담기 위해서 바구니가 이동해야 하는 거리의 최솟값
"""

N, M = map(int, input().split())

J = int(input())
current = 1
result = 0

for i in range(J):
    a = int(input())

    if current <= a <= current + M - 1:
        continue
    elif a < current:
        result += current - a
        current -= current - a
    else:
        result += a - (current + M - 1)
        current += a - (current + M - 1)

print(result)