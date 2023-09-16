"""
입력 : 첫째 줄 - N, M (행렬의 크기)
      이후 - 연료 값 (행렬만큼)
출력 :  필요한 최소 연료의 값
"""
import sys
from sys import stdin

N, M = map(int, stdin.readline().split())
oil = []
direction = [-1, 0, 1]

for i in range(N):
    oil_tmp = list(map(int, stdin.readline().split()))
    oil.append(oil_tmp)

def DFS(row, col, d, low, answer):
    if row == N - 1:
        return min(low, answer)

    for k in direction:
        if k != d:
            if 0 <= row < N and 0 <= col + k < M:
                low = DFS(row + 1, col + k, k, low, answer + oil[row + 1][col + k])
    return low


low = int(sys.maxsize)

for j in range(M):
    low = min(DFS(0, j, 2, low, oil[0][j]), low)

print(low)
