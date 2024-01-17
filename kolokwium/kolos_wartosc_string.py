n = int(input())

values = {}
res = []
for _ in range(n):
    s = input().split()
    op = s[1]
    flag = True
    if '+' in op:
        flag = True
    elif '-' in op:
        flag = False
    if s[0] in values and flag:
        values[s[0]] += int(s[-1])
    elif s[0] in values and flag == False:
        values[s[0]] -= int(s[-1])
    else:
        values[s[0]] = int(s[-1])

    sort_l = sorted(values.items(), key=lambda x: x[1], reverse=True)

    min_val = min(sort_l, key=lambda x: x[1])[1]
    max_val = max(sort_l, key=lambda x: x[1])[1]

    c_min = 0
    c_max = 0
    for el in sort_l:
        if el[1] == min_val:
            c_min += 1
        if el[1] == max_val:
            c_max += 1

    if c_min == 1:
        res.append(sort_l[-1][0])
    if c_max == 1:
        res.append(sort_l[0][0])
    else:
        continue

s = sorted(set(res))
print(*s)

