"""
입력 : 첫째 줄 - N (보드 크기)
      이후 - 사탕의 색상 (N만큼)
출력 : 상근이가 먹을 수 있는 사탕의 최대 개수
"""

from sys import stdin

N = int(stdin.readline())
candy = []
max_cnt = 0

for c in range(N):
    candy_tmp = list(map(str, stdin.readline()))
    candy.append(candy_tmp)


def row():
    global max_cnt

    for k in range(N):
        cnt = 1
        for l in range(N - 1):
            if candy[k][l] == candy[k][l+1]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1


def column():
    global max_cnt

    for k in range(N):
        cnt = 1
        for l in range(N - 1):
            if candy[l][k] == candy[l + 1][k]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1


for i in range(N):
    for j in range(N - 1):
        if candy[i][j] != candy[i][j + 1]:  # 가로 비교
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            row()
            column()
            candy[i][j + 1], candy[i][j] = candy[i][j], candy[i][j + 1]  # 원위치

        if candy[j][i] != candy[j + 1][i]:  # 세로 비교
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]
            row()
            column()
            candy[j + 1][i], candy[j][i] = candy[j][i], candy[j + 1][i]

print(max_cnt)
