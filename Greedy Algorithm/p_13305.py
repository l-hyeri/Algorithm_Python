"""
입력 : 첫째 줄 - 자연수 N (도시 개수)
      둘째 줄 - 도로 길이 (N-1 개)
      셋째 줄 - 주유소의 리터당 가격 (N 개)
출력 : 제일 왼쪽 도시에서 제일 오르쪽 도시로 가는 최소 비용 출력

[처음 코드 : 17점]
N = int(input())
road = list(map(int, input().split()))  # 도로 길이
oil = list(map(int, input().split()))  # 주유소
min_oil = 0  # 주유 최소값 저장
cost = 0  # 최종 가격 출력

sum_road = sum(road)

if oil[N - 1] == min(oil):
    temp = oil.copy()
    temp.sort()
    min_oil = temp[1]
else:
    min_oil = min(oil)

for i in range(N - 2):
    if oil[i] == min_oil:
        cost += min_oil * sum_road
        sum_road = 0
    else:
        cost += oil[i] * road[i]
        sum_road -= road[i]

print(cost)
"""

N = int(input())
road = list(map(int, input().split()))  # 도로 길이
oil = list(map(int, input().split()))  # 주유소
min_oil = oil[0]
cost = 0

for i in range(N - 1):
    if oil[i] < min_oil:
        min_oil = oil[i]

    cost += (min_oil * road[i])

print(cost)
