"""
입력 :
출력 :
"""
list = []
temp1, temp2 = 0, 0

for i in range(9):
    num = int(input())
    list.append(num)

list = sorted(list)
sum_list = sum(list)

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if sum_list - list[i] - list[j] == 100:
            temp1 = list[i]
            temp2 = list[j]
list.remove(temp1)
list.remove(temp2)

for i in range(len(list)):
    print(list[i])
