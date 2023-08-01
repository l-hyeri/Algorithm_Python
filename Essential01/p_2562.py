"""
입력 : 첫째 줄 ~ 아홉 번째 줄 (자연수)
출력 : 첫째 줄 - 최댓값, 둘째 줄 - 최댓값의 인덱스 번호
"""

list = []
result = []

for i in range(9):
    a = int(input())
    list.append(a)
    result = sorted(list)

print(result[8])
print(list.index(result[8]) + 1)
