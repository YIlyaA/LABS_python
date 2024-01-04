n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
count = 0
horizontal_pos = []
vertical_pos = []

for line in range(n):
    for col in range(n):
        if matrix[line][col] == 1:
            count += 1
            horizontal_pos.append(line + 1)
            vertical_pos.append(col + 1)

res_h = list(horizontal_pos)
res_v = list(vertical_pos)


def check_division(h_p, v_p, i, j):
    i1, j1 = h_p[i], v_p[i]
    i2, j2 = h_p[j], v_p[j]
    if j2 % j1 == 0 and i2 % i1 == 0:
        # print(f'{j2} % {j1} and {i2} % {i1}')
        return abs(i2 - i1) + abs(j2 - j1)
    else:
        return 1000


result = []
for i in range(count - 1):
    for j in range(i, count):
        result.append(check_division(horizontal_pos, vertical_pos, i, j))

res = []
for el in result:
    if 0 < el < 1000:
        res.append(el)

if len(res) == 0:
    print(1000)
else:
    print(min(res))

