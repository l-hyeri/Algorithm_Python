"""
입력 : 첫줄 - 테스트 케이스 T, 정수 입력 A, B
출력 : A+B
"""

T = int(input())
list = []

for i in range(T):
    A, B = map(int, input().split())
    list.append(A + B)

for j in range(T):
    print(list[j])
