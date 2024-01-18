def s(matrix, n):

    def is_valid(up, left, right, down):
        val = set()
        for i in range(up, right + 1):
            for j in range(left, down + 1):
                if matrix[i][j] in val:
                    return False
                val.add(matrix[i][j])
        return True

    ar = 0

    for up in range(n):
        for left in range(n):
            for right in range(up, n):
                for down in range(left, n):
                    if is_valid(up, left, right, down):
                        area = (right - up + 1) * (down - left + 1)
                        ar = max(ar, area)

    return ar


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(s(matrix, N))
