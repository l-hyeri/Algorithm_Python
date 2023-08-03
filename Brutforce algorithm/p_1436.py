"""
입력 : 자연수 N
출력 : N번째 영화의 제목에 들어간 수
"""

N = int(input())
cnt = 0  # 몇번째 영화인지 확인하기 위함
title = 666  # 제목 (666번부터 시작)

while True:
    if "666" in str(title):
        cnt += 1

    if cnt == N:
        print(title)
        break

    title += 1
