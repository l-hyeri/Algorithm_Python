"""
입력 : 첫째 줄 - N과 K
      이후 - 동전의 가치 A (오름차순)
출력 : K원을 만드는데 필요한 동전 개수 (최솟값)
"""
from sys import stdin

N, K = map(int, stdin.readline().split())
arr = []
cnt = 0

for i in range(N):
    arr.append(int(stdin.readline()))

arr.sort(reverse=True)

for j in arr:
    cnt += (K // j)
    K %= j
print(cnt)
