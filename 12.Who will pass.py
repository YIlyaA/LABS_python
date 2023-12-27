n = int(input())
matrix = []
new_matrix = []

for i in range(n):
    linia = [int(x) for x in input().split()]
    matrix.append(linia)
for i in range(n):
    for j in range(n):
        if (matrix[i][j] >= 3):
            new_matrix.append(1)
        else:
            if (i == 0 and j == 0):
                if (((matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i][j + 1]) / 3) >= 3):
                    new_matrix.append(1)
                else:
                    new_matrix.append(0)
            elif (i == n - 1 and j == 0):
                if (((matrix[i - 1][j] + matrix[i - 1][j + 1] + matrix[i][j + 1]) / 3) >= 3):
                    new_matrix.append(1)
                else:
                    new_matrix.append(0)
            elif (i == 0 and j == n - 1):
                if (((matrix[i][j - 1] + matrix[i + 1][j] + matrix[i + 1][j - 1]) / 3) >= 3):
                    new_matrix.append(1)
                else:
                    new_matrix.append(0)
            elif (i == n - 1 and j == n - 1):
                if (((matrix[i][j - 1] + matrix[i - 1][j] + matrix[i - 1][j - 1]) / 3) >= 3):
                    new_matrix.append(1)
                else:
                    new_matrix.append(0)

            elif (i != 0 and j == 0 and i != n - 1):
                if (((matrix[i][j + 1] + matrix[i - 1][j + 1] + matrix[i - 1][j] + matrix[i + 1][j] + matrix[i + 1][
                    j + 1]) / 5) >= 3):
                    new_matrix.append(1)
                else:
                    new_matrix.append(0)
            elif (i == 0 and j != 0 and j != n - 1):
                if (((matrix[i][j - 1] + matrix[i][j + 1] + matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][
                    j + 1]) / 5) >= 3):
                    new_matrix.append(1)
                else:
                    new_matrix.append(0)
            elif (i != 0 and j == n - 1 and i != n - 1):
                if (((matrix[i][j - 1] + matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i + 1][j] + matrix[i + 1][
                    j - 1]) / 5) >= 3):
                    new_matrix.append(1)
                else:
                    new_matrix.append(0)
            elif (i == n - 1 and j != 0 and j != n - 1):
                if (((matrix[i][j - 1] + matrix[i][j + 1] + matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][
                    j + 1]) / 5) >= 3):
                    new_matrix.append(1)
                else:
                    new_matrix.append(0)
            elif (i != 0 and j != 0 and i != n - 1 and j != n - 1):
                if (((matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1] + matrix[i][j - 1] + matrix[i][
                    j + 1] + matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]) / 8) >= 3):
                    new_matrix.append(1)
                else:
                    new_matrix.append(0)
for i in range(0, n * n, n):
    for j in range(n):
        print(new_matrix[i + j], end=' ')
    print()
