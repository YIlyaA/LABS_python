def spiral_matrix(matrix, n):
    top, bottom, left, right = 0, n - 1, 0, n - 1
    spiral = []
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            spiral.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            spiral.append(matrix[i][right])
        right -= 1

        for i in range(right, left - 1, -1):
            spiral.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            spiral.append(matrix[i][left])
        left += 1

    return spiral


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
spiral = spiral_matrix(matrix, n)
print(*spiral)
