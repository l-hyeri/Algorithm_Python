"""
입력 : 첫째 줄 - N, K
      이후 - 국가를 나타내는 정수 (공백) 금 (공백) 은 (공백) 동
출력 : 국가 K의 둥수를 정수로 출력
"""

from sys import stdin

N, K = map(int, stdin.readline().split())
arr = []
cnt = 1

for i in range(N):
    result = list(map(int, stdin.readline().split()))

    if result[0] != K:
        arr.append(result)
    else:
        standard = result

for j in range(len(arr)):
    if standard[1] < arr[j][1]:
        cnt += 1
    elif standard[1] == arr[j][1]:
        if standard[2] < arr[j][2]:
            cnt += 1
        elif standard[2] == arr[j][2]:
            if standard[3] < arr[j][3]:
                cnt += 1
print(cnt)
