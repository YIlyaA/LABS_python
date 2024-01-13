N, n = [int(x) for x in input().split()]
matrix = []
max = 0
for i in range(N):
    line = [int(x) for x in input().split()]
    matrix.append(line)
for a in range(N - n + 1):
    for b in range(N - n + 1):
        matrix2 = []
        for c in range(a, a + n):
            line = []
            for d in range(b, b + n):
                line.append(matrix[c][d])
            matrix2.append(line)
        s = 0
        print(matrix2)
        for i in range(n):
            for j in range(n):
                for h in range(n):
                    s = s + matrix2[i][h] * matrix2[h][j]
        if (s > max):
            max = s
print(max)
