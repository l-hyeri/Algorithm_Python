"""
입력 : 첫째 줄 - N (운동기구 개수)
      이후 - T (각 운동기구 근손실 정도)
출력 : M의 최솟값
"""
from sys import stdin

N = int(stdin.readline())
T = list(map(int, stdin.readline().split()))
M = []

T.sort()

if N % 2 == 0:  # 짝수
    for i in range(N // 2):
        result = T[i] + T[N - 1 - i]
        M.append(result)

else:  # 홀수 (마지막 하나 제외 후 계산)
    M.append(T[N - 1])
    for i in range((N - 1) // 2):
        result = T[i] + T[N - 2 - i]
        M.append(result)

print(max(M))
