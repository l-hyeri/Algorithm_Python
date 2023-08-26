"""
입력 : 자연수 N (1이상 1000이하)
출력 : 2xN 크기의 직사각형을 채우는 방법 수 % 10007
"""

N = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[N])
