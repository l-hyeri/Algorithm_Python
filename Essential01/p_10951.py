"""
입력 : 여러 개 테스트 케이스 , 정수 A,B 입력
출력 : A+B 출력
"""

list = []

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break
