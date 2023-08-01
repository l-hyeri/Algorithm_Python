"""
입력 : 첫째 줄 - 정수 N, 둘째 줄 - N개의 정수 공백 구분
출력 : 최솟값 (공백) 최댓값
"""

N = int(input())
a = list(map(int, input().split()))

print(min(a), max(a))
