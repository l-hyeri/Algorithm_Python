"""
입력 : 돌 개수 N (자연수)
출력 : 상근이가 이김 - SK 출력, 창영이가 이김 - CY 출력
"""

# 돌 개수 입력받기
N = int(input())

# 리스트 초기화
dp = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = int(i / 3) + int(i % 3)
    # print(i, dp[i])

if dp[N] % 2 == 1:
    print('SK')
else:
    print('CY')