"""
입력 : 첫쨰 줄 - N (스위치 개수)
      둘째 줄 - 스위치 상태 (N만큼)
      셋째 줄 - 학생 수
      이후 - 성별 (꽁백) 받은수
출력 : 바뀐 스위치 상태 출려 (한줄에 20개씩)
"""

from sys import stdin

def change(s_num):
    if switch[s_num] == 0:
        switch[s_num] = 1
    else:
        switch[s_num] = 0
    return switch


N = int(stdin.readline())
switch = list(map(int, stdin.readline().split()))
S = int(stdin.readline())

for i in range(S):
    gender, num = map(int, stdin.readline().split())

    if gender == 1:
        for j in range(N):
            if (j + 1) % num == 0:
                change(j)
    else:
        change(num - 1)

        for j in range(N // 2):
            if num - j - 1 < 1 or num + j + 1 > N:
                break
            else:
                if switch[num - j - 2] == switch[num + j]:
                    change(num - j - 2)
                    change(num + j)
                else:
                    break

for k in range(1, len(switch) + 1):
    print(switch[k - 1], end=' ')

    if k % 20 == 0:
        print()
