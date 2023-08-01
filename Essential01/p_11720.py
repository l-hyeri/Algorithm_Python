"""
입력 : 첫째 줄 - 숫자 개수 N , 둘째 줄 : 숫자
출력 : N개의 합
"""

N = int(input())
A = input()
result = 0

for i in range(N):
    result += int(A[i])

print(result)
