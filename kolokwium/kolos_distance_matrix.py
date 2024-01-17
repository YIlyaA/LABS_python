import copy

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


def check_higher(x, y, mat, n):
    distances = []
    for i in range(n):
        for j in range(n):
            if mat[x][y] < mat[i][j]:
                dis = abs(x - i) + abs(y - j)
                print('dis: ', dis, ' ind_x: ', x, i, 'y_ind: ', y, j)
                distances.append(dis)
    if len(distances) == 0:
        return -1
    return min(distances)


new_matrix = copy.deepcopy(matrix)
for i in range(n):
    for j in range(n):
        nn = check_higher(i, j, matrix, n)
        print(nn)
        print(matrix)
        new_matrix[i][j] = nn

for el in new_matrix:
    print(*el)
