"""
입력 : 첫째 줄 - N,M (N : 스크린 크기, M : 바구니 크기)
      둘째 줄 - 떨어지는 사과의 개수 J (1이상 20이하)
      이후 - J개의 줄에 사과가 떨어지는 위치
출력 : 모든 사과를 담기 위해서 바구니가 이동해야 하는 거리의 최솟값
"""

N, M = map(int, input().split())
J = int(input())  # 사과 개수

basket = 1  # 바구니 현 위치
result = 0

for i in range(J):
    apple = int(input())

    if basket <= apple <= basket + M - 1:  # 바구니 안에 사과가 위치 (이동 x)
        continue

    elif basket < apple:  # 바구니보다 오른쪽에 사과가 위치
        result += apple - (basket + M - 1)
        basket += apple - (basket + M - 1)

    else:  # 바구니보다 왼쪽에 사과가 위치
        result += basket - apple
        basket -= basket - apple

print(result)
