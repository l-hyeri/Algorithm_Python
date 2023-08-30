"""
입력 : 첫째 줄 - N (공백) M -> N = 수의 개수, M = 합을 구해야 하는 횟수
출력 : M개의 줄에 입력으로 주어진 i번쨰 수부터 j번째 수까지의 합

[시간초과 발생]
N, M = map(int, input().split())
arr = list(map(int, input().split()))

for k in range(M):
    i, j = map(int, input().split())
    print(sum(arr[i - 1: j]))

[해결 방법]
1. sys.stdin.readline을 통한 input 사용
2. 미리 배열의 누적 합을 구함
3. s[end]-s[start-1]
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
temp = [0]  # 누적합을 저장하기 위한 배열 생성 (index 1부터 시작하기 때문에 0 미리 저장)
num = 0

for m in arr:
    num += m
    temp.append(num)

for n in range(M):
    i, j = map(int, input().split())
    print(temp[j] - temp[i - 1])
