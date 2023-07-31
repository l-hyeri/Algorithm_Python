"""
입력 : 정수 A,B
출력 : A+B (0,0일 경우 break)
"""

while True:
    A, B = map(int, input().split())

    if A == 0 & B == 0:
        break

    print(A + B)
