"""
입력 : 자연수 N
출력 : N! 결과값의 0의 개수

[답은 나오지만 Wrong Answer 뜨는 코드]
N = int(input())
num = 1
cnt = 0

for i in range(1, N + 1): for문을 통해 factorial 값을 구하는 것이 아닌 함수 쓰는 것으로 해결
    num *= i

num = str(num)

for i in range(len(num)):
    if int(num[i]) == 0: int로 변환하지 않고 문자열로 바로 비교
        cnt += 1

    else:
        break

print(cnt)
"""
import math

N = int(input())
num = str(math.factorial(N))  # 입력한 값을 문자열로 변환

cnt = 0

for i in range(len(num) - 1, -1, -1):  # 역순으로 조회
    if num[i] == '0':
        cnt += 1
    else:
        break
print(cnt)
