"""
입력 : 거스름돈 액수 N
출력 : 거스름돈 동전의 최소 개수 출력 (거슬러 줄 수 없는 경우 -1 출력)
"""

N = int(input())
cnt = 0

while True:
    if N % 5 == 0:
        cnt += N // 5
        break

    else:
        N -= 2
        cnt += 1

    if N < 0:
        break

if N < 0:
    print(-1)
else:
    print(cnt)
