"""
입력 : 문자열 S (소문자로만 이루어짐)
출력 : 단어에 포함되어 있는 각 문자의 개수 출력 (공백구분)
"""

S = input()
arr = [0] * 26

for i in S:
    arr[ord(i) - 97] += 1

for j in arr:
    print(j, end= " ")
