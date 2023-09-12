"""
입력 :
출력 :
"""

from sys import stdin

P = int(stdin.readline())

for i in range(P):
    cnt = 0
    tmp = 0
    height = list(map(int, stdin.readline().split()))

    for j in range(1, 20):
        for k in range(j + 1, 21):
            if height[j] < height[k]:
                continue
            else:
                tmp = height[k]
                height[k] = height[j]
                height[j] = tmp
                cnt += 1

    print(height[0], cnt)
