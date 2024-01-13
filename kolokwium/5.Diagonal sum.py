n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
rev_matrix = []
for el in matrix:
    new_el = list(reversed(el))
    rev_matrix.append(new_el)


def diag_sum_col(mat):
    # Vertical line
    diag_sum = []
    for i in range(n):
        x, y = i, 0
        res = 0
        r = m
        if n <= m:
            r = n - x
        if n > m and n - x < m:
            r = n - x
        for d in range(r):
            res += mat[x + d][y + d]
        diag_sum.append(res)
    diag_sum.pop(0)
    return diag_sum


def diag_sum_row(mat):
    diag_sum = []
    for i in range(m):
        x, y = 0, i
        res = 0
        r = n
        if n >= m:
            r = m - y
        if n < m and m - y < n:
            r = m - y
        for d in range(r):
            res += mat[x + d][y + d]
        diag_sum.append(res)
    return diag_sum


diag = diag_sum_col(matrix) + diag_sum_row(matrix) + diag_sum_col(rev_matrix) + diag_sum_row(rev_matrix)

res_list = set(diag)
print(max(res_list))
