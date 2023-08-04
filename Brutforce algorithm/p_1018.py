"""
입력 : 첫째 줄 - N,M 보드 크기, 이후 - 보드 상태 (W,B)
출력 : 다시 칠해야 하는 정사각형 개수 최솟값
"""

N, M = map(int, input().split())
list = []  # 보드 상태를 저장하기 위함
cnt = 0  # 다시 칠해야 하는 정사각형 개수 count하기 위함
result = []  # 결과값을 비교하기 위함

for i in range(N):
    list.append(input())

for a in range(N - 7):  # 보드 크기를 8x8로 자르기 위함
    for b in range(M - 7):
        white = 0  # 흰색으로 바꿔야 하는 경우
        black = 0

        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:  # 짝수인 경우
                    if list[i][j] != 'B':
                        black += 1
                    else:
                        white += 1
                else:
                    if list[i][j] != 'B':
                        white += 1
                    else:
                        black += 1

        result.append(black)
        result.append(white)

print(min(result))
