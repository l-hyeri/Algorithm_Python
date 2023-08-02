"""
입력 : 자연수 N
출력 : 생성자 출력 (없는 경우 0출력)
"""

N = int(input())
result = 0

for i in range(1, N + 1):
    num = sum(map(int, str(i)))

    if i + num == N:
        result = i
        break
print(result)
