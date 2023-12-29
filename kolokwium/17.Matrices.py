def check_trans_matrix(m1, m2, n):
    for i in range(n):
        for j in range(n):
            afo_matrix = []  # after operation matrix
            col_matrix = []
            new_matrix = list(m1)
            del new_matrix[i]
            for k in range(n):
                line = []
                for l in range(len(new_matrix)):
                    line.append(new_matrix[l][k])
                col_matrix.append(line)  # creating col matrix
            del col_matrix[j]

            for r in range(len(col_matrix)):
                lin = []
                for s in range(len(col_matrix)):
                    lin.append(col_matrix[s][r])
                afo_matrix.append(lin)

            if afo_matrix == m2:
                return True
    return False


n = int(input())
matrix_1 = [input().split() for _ in range(n)]
matrix_2 = [input().split() for _ in range(n - 1)]
print(check_trans_matrix(matrix_1, matrix_2, n))
