"""
입력 : 자연수 N (1이상 100000이하)
출력 : 주어진 자연수를 제곱수의 합으로 나타낼 때 제곱수 항의 최소 개수

[답은 맞지만 Wrong Answer 뜨는 코드]
N = int(input())

dp = [0] * 1000001

dp[1] = 1
num1 = 1

for i in range(2, N + 1):
    if pow(num1, 2) <= i:  # 최대 제곱수 찾기
        num1 += 1
        # if dp[pow(num1 - 1, 2)] == 0:
        #     dp[pow(num1 - 1, 2)] = 1  # dp[제곱수]=0일경우 1로 증가

    num2 = i - pow(num1 - 1, 2)
    dp[i] = 1 + dp[num2]

print(dp[N])
"""

N = int(input())
dp = [k for k in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
print(dp[N])
