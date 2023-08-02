"""
입력 : 첫 줄 - 수의 개수 N, 이후 - N개의 자연수
출력 : 소수의 개수 출력
"""
N = int(input())
num = list(map(int, input().split()))
count = 0

for i in num:
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
print(count)
