"""
입력 : 첫쨰 줄 - 테스트 케이스 T
      두번째 줄 - 정수 N (참가 인원)
      세번쨰 줄 - 정수 M (팀 개수 만큼)
출력 : 우승팀의 번호 출력
"""

from sys import stdin

T = int(stdin.readline())

for i in range(T):
    N = int(stdin.readline())
    M = list(map(int, stdin.readline().split()))
    team = {}

    for j in range(N):  # 팀 인원수 count
        if M[j] not in team:
            team[M[j]] = [1, [], 0]  # {팀 번호 : [팀 인원, [점수 리스트], 점수 합계}

        else:
            team[M[j]][0] += 1

    contain = set(k for k, v in team.items() if v[0] < 6)  # 인원이 6명이 넘지 않은 팀 번호 저장

    score = 1
    for k in range(N):
        if M[k] not in contain:
            team[M[k]][1].append(score)

            if len(team[M[k]][1]) <= 4:
                team[M[k]][2] += score

            score += 1

    result = []
    for k, v in team.items():
        if len(v[1]) != 0 and v[2] != 0:
            result.append([k, v[1][4], v[2]])

    final = sorted(result, key=lambda x: (x[2], x[1]))
    print(final[0][0])
