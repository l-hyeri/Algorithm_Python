"""
입력 : N, K
출력 :  N, K를 이항계수로 계산한 결과값 % 10007
"""

N, K = map(int, input().split())
result1 = 1
result2 = 1

for i in range(K):
    result1 *= N
    N -= 1

for j in range(K):
    result2 *= K
    K -= 1

print((result1 // result2) % 10007)
