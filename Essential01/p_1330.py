"""
입력 : 정수 A, B
출력 : 큰 경우 > , 작은 경우 < , 같은 경우 ==
"""

A, B = map(int, input().split())

if A>B:
    print(">")
elif A<B:
    print("<")
else:
    print("==")