"""
입력 : 첫째 줄 - 카드 개수 N (공백) 슷자 M , 둘째 줄 - 카드 N
출력 : M을 넘지 않으면서 최대한 가까운 카드 3개의 합
"""

N, M = map(int, input().split())
num = list(map(int, input().split()))
ans = 0

for i in range(N):
    for j in range(i + 1, N):
        for z in range(j+1, N):
            result = num[i] + num[j] + num[z]

            if M < result:
                continue
            else:
                ans = max(ans, result)
print(ans)
