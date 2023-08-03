"""
입력 : 첫째 줄 - 테스트케이스 T, 이후 - 자연수 K
출력 :  3개의 삼각함수로 표현되면 1, 아니면 0
"""
form = []
sum = [0] * 1001  # 3수의 합을 저장하기 위한 리스트 생성

for n in range(1, 46):  # 공식에 미리 대입
    form.append(n * (n + 1) // 2)

for i in form:
    for j in form:
        for k in form:
            num = i + j + k
            if num <= 1000:
                sum[num] = 1

T= int(input())

for i in range(T):
    print(sum[int(input())])
