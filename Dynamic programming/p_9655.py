"""
입력 : 돌 개수 N (자연수)
출력 : 상근이가 이김 - SK 출력, 창영이가 이김 - CY 출력
"""

N = int(input())

dp = [0] * 1001  # 미리 trun횟수를 저장하기 위한 리스트 (N이 1~1000이기때문에 1001번까지 리스트 생성)
dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(4, N + 1):
    dp[i] = min(dp[i - 1], dp[i - 3]) + 1

if dp[N] % 2 == 1:
    print('SK')
else:
    print('CY')