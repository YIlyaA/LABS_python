def max_rectangle_sum(matrix_size, matrix):
    max_sum = 0

    for i in range(matrix_size):
        temp = [0] * matrix_size

        for j in range(i, matrix_size):
            for k in range(matrix_size):
                temp[k] += matrix[j][k]

            current_sum = 0
            max_current_sum = 0

            for k in range(matrix_size):
                current_sum = max(0, current_sum + temp[k])
                max_current_sum = max(max_current_sum, current_sum)

            max_sum = max(max_sum, max_current_sum)

    return max_sum


# Sample Input
matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    row = list(map(int, input().split()))
    matrix.append(row)

# Sample Output
result = max_rectangle_sum(matrix_size, matrix)
print(result)
