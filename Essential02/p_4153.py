"""
입력 : 여러개의 테스트 케이스, 마지막줄 0 0 0 , 3개의 정수 입력
출력 : 직각 삼각형이면 right, 아니면 wrong
"""

while True:
    a = list(map(int, input().split()))

    if a[0] == 0 & a[1] == 0 & a[2] == 0:
        break

    a = sorted(a)

    if a[2] * a[2] == a[0] * a[0] + a[1] * a[1]:
        print("right")
    else:
        print("wrong")