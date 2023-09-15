"""
입력 : 첫째 줄 - N (현재 리스트에 있는 점수 개수) (공백) 태수의 새로운 점수, P (랭킹에 올라갈 수 있는 점수 개수)
출력 : 새로운 점수가 랭킹 리스트에서 몇 등인지 출력

[방법 1]
from sys import stdin

N, S, P = map(int, stdin.readline().split())

if N == 0:
    print(1)
else:
    current = list(map(int, stdin.readline().split()))

    if N == P and current[-1] >= S:
        print(-1)
    else:
        result = N + 1
        for i in range(N):
            if current[i] <= S:
                result = i + 1
                break
        print(result)

"""
from sys import stdin

N, S, P = map(int, stdin.readline().split())

if N == 0:
    print(1)

else:
    current = list(map(int, stdin.readline().split()))
    current.append(S)
    current.sort(reverse=True)
    idx = current.index(S) + 1  # 현재 입력된 S가 있는 등수

    if idx > P:
        print(-1)

    else:
        if N == P and S == current[-1]:
            print(-1)
        else:
            print(idx)
