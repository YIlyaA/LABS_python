N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

all_matrix = []
for n in range(3, N + 1, 2):
    for a in range(N - n + 1):
        for b in range(N - n + 1):
            matrix2 = []
            for c in range(a, a + n):
                line = []
                for d in range(b, b + n):
                    line.append(matrix[c][d])
                matrix2.append(line)
            all_matrix.append(matrix2)


def check_xt(mat):
    length = len(mat)
    sum1 = 0
    sum2 = 0
    for i in range(length):
        sum1 += mat[i][i] + mat[-i - 1][i]
    for j in range(length):
        sum2 += mat[j][length // 2] + mat[0][j]
    sum1 -= mat[length//2][length//2]
    sum2 -= mat[0][length//2]
    if sum1 == sum2:
        return length
    else:
        return 0


l = []
for mat in all_matrix:
    res = check_xt(mat)
    if res == 0:
        continue
    else:
        l.append(res)

if len(l) == 0:
    print(1)
else:
    print(max(l))
