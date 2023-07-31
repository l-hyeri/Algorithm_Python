"""
입력 : 정수 N (1~9사이)
출력 : N단 출력 (구구단)
"""

N = int(input())

for i in range(1, 10):
    print(N, "*", i, "=", N * i)
