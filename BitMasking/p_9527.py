"""
입력 : 두 자연수 A, B
출력 : 1의 개수를 세어 출력

[시간초과]
def bitCount(X):
    if X == 0:
        return 0
    return X % 2 + bitCount(X // 2)


A, B = map(int, input().split())
result = 0

for i in range(A, B + 1):
    result += bitCount(i)

print(result)
"""

def bitCount(X):
    cnt = 0
    bin_num = bin(X)[2:]
    length = len(bin_num)

    for i in range(length):
        if bin_num[i] == '1':
            pow = length - i - 1
            cnt += arr[pow]
            cnt += (X - 2 ** pow + 1)
            X = X - 2 ** pow
    return cnt


A, B = map(int, input().split())
arr = [0 for x in range(60)]

for i in range(1, 60):
    arr[i] = 2 ** (i - 1) + 2 * arr[i - 1]

print(bitCount(B)-bitCount(A-1))