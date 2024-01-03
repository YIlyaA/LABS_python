def smallest_number(matrix, n):
    col_matrix = column_matrix(matrix, n)
    new_matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            number = matrix[i][j]
            column = col_matrix[j]
            row = matrix[i]
            print(f'Column and row: {column}, {row}')
            if number == min(row) and number == min(column):
                line.append(-1)
            else:
                num = check_smaller_num(number, column, row, i, j)
                line.append(num)
            print('---------------------------------------------------')
        new_matrix.append(line)
    return new_matrix


def check_smaller_num(num, col, row, i, j):
    numbers1 = {}
    numbers2 = {}
    print("El: ", num)
    for el in range(len(row)):
        if num == min(row):
            numbers1[num] = 0
            break
        if row[el] < num:
            if row[el] in numbers1:
                numbers1[row[el]] = min(abs(el - j), numbers1[row[el]])
            else:
                numbers1[row[el]] = abs(el - j)

    print("Numbers ", numbers1)

    for k in range(len(col)):
        if num == min(col):
            numbers2[num] = 0
            break
        if col[k] < num:
            if row[k] in numbers2:
                numbers2[col[k]] = min(abs(k - i), numbers2[col[k]])
            else:
                numbers2[col[k]] = abs(k - i)
    print("Numbers ", numbers2)

    min_key1 = min(numbers1, key=lambda x: numbers1[x])
    min_key2 = min(numbers2, key=lambda x: numbers2[x])
    print("KEYS: ", min_key1, min_key2, numbers1[min_key1], numbers2[min_key2])

    if numbers1[min_key1] == numbers2[min_key2]:
        print("ANS: ", min(min_key1, min_key2))
        return min(min_key1, min_key2)
    if numbers1[min_key1] > numbers2[min_key2] != 0:
        print("ANS: ", numbers2[min_key2])
        return min_key2
    if numbers2[min_key2] > numbers1[min_key1] != 0:
        print("ANS: ", numbers2[min_key2])
        return min_key1
    if numbers1[min_key1] == 0:
        print("ANS: ", numbers2[min_key2])
        return min_key2
    if numbers2[min_key2] == 0:
        print("ANS: ", numbers1[min_key1])
        return min_key1


def column_matrix(matrix, n):
    col_matrix = []
    for i in range(n):
        t = []
        for j in range(n):
            t.append(matrix[j][i])
        col_matrix.append(t)
    return col_matrix


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = smallest_number(matrix, n)
for el in result:
    print(*el)
