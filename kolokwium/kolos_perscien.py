n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

diag_matrix = []
for i in range(n):
    t = []
    for j in range(n):
        t.append(matrix[j][i])
    diag_matrix.append(t)


def pierscien(ind, mat):
    sum1 = 0
    for j in range(ind, n - ind):
        sum1 += mat[ind][j] + mat[-ind - 1][j]
    return sum1


summ = []
for i in range(n // 2):
    s = pierscien(i, matrix) + pierscien(i, diag_matrix) - matrix[i][i] - matrix[i][-i - 1] - matrix[-i - 1][i] - \
        matrix[-i - 1][-i - 1]
    print(s, end=" ")
if n % 2 == 1:
    print(matrix[n//2][n//2])
