def sum_list(l, start, end):
    summ = 0
    new_list = l[start:end+1]
    for el in new_list:
        summ += el
    return summ


l = list(map(int, input().split()))
k = int(input())
i_j = [list(map(int, input().split())) for _ in range(k)]

for indexs in i_j:
    start = indexs[0]
    end = indexs[1]
    print(sum_list(l, start, end))

