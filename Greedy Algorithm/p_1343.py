"""
입력 : 보드판 크기 (최대 50)
출력 :  사전순으로 가장 앞서는 답 출력 , 덮을 수 없을 경우 -1 출력
    AAAA와 BB로 X로 이루어진 보드판을 덮어야 함. '.'는 제외

[방법1]
board = input()
result = ''
i = 0

while i < len(board):
    if board[i:i + 4] == 'XXXX':
        result += 'AAAA'
        i += 4

    elif board[i:i + 2] == 'XX':
        result += 'BB'
        i += 2

    else:
        result += board[i]
        i += 1

if 'X' not in result:
    print(result)
else:
    print(-1)
"""

board = input()
board = board.replace('XXXX','AAAA')
board= board.replace('XX','BB')

if 'X' not in board:
    print(board)
else:
    print(-1)
