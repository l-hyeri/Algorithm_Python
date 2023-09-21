"""
입력 : 첫째 줄 - N (화단의 한 변의 길이)
      이후 - 화단의 지점당 가격 (N X N만큼)
출력 : 꽃을 심기 위한 최소 비용
"""
from sys import stdin


def check(i, j, visited):
    for idx in range(4):
        vi = i + direction[idx][0]
        vj = j + direction[idx][1]

        if (vi, vj) in visited:
            return False

    return True


def DFS(visited, total):
    global result_cost

    if total >= result_cost:
        return
    if len(visited) == 15:
        result_cost = min(result_cost, total)

    else:
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if check(i, j, visited) and (i, j) not in visited:
                    d_temp = [(i, j)]
                    temp_cost = cost[i][j]

                    for idx in range(4):
                        vi = i + direction[idx][0]
                        vj = j + direction[idx][1]

                        d_temp.append((vi, vj))
                        temp_cost += cost[vi][vj]

                    DFS(visited + d_temp, total + temp_cost)


N = int(stdin.readline())
cost = [list(map(int, stdin.readline().split())) for _ in range(N)]

result_cost = int(1e9)
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DFS([], 0)

print(result_cost)
