def will_pass(matrix, n):
    col_matrix = list(column_matrix(matrix))
    new_matrix = list(map(list, matrix))
    for i in range(n):
        for j in range(n):
            if matrix[i][j] >= 7:
                new_matrix[i][j] = 1
            else:
                if sum_of_row_and_col(col_matrix[j], matrix[i], j, i) >= 7:
                    new_matrix[i][j] = 1
                else:
                    new_matrix[i][j] = 0
    return new_matrix


def sum_of_row_and_col(col, row, j, i):
    summ = []
    for el in row:
        if el >= row[j]:
            summ.append(el)

    for el in col:
        if el >= col[i]:
            summ.append(el)

    summ.remove(row[j])
    return sum(summ) / len(summ)


def column_matrix(matrix):
    col_matrix = []
    for i in range(len(matrix)):
        t = []
        for j in range(len(matrix)):
            t.append(matrix[j][i])
        col_matrix.append(t)
    return col_matrix


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
mtrx = will_pass(matrix, n)
for line in mtrx:
    print(*line)
