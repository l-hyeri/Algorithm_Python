"""
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때,
각각의 로프에는 모두 w/k만큼의 중량이 걸리게 됨.
입력 : 첫째 줄 - 정수 N
      이후 - 각 로프가 버틸 수 있는 최대 중량 (10000을 넘지 않는 자연수)
출력 : 물체의 최대 중량을 출력
"""

N = int(input())
arr = []
result = []

for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

for j in range(N):
    result.append(arr[j] * (j + 1))

print(max(result))
