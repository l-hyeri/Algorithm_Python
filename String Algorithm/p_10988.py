"""
입력 : 단어 (소문자)
출력 : 팰린드롬이면 1, 아니면 0

[정답은 맞음 - 비효율적인 코드]
from copy import copy

S = input()
arr = []
check = 0

for i in range(len(S)):
    arr.append(S[i])

list = copy(arr)
list.reverse()

for j in range(len(S)):
    if arr[j] == list[j]:
        continue
    else:
        check += 1
        print(0)
        break

if check == 0:
    print(1)

"""

S = list(str(input()))

if list(reversed(S)) == S:
    print(1)
else:
    print(0)
