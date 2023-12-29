def find_position_zero(matrix):
    indexs = []
    for line in range(len(matrix)):
        for el in range(len(matrix[0])):
            if matrix[line][el] == 0:
                index_c = el
                index_w = line
                indexs.append([index_c, index_w])
    return indexs


def zero_line_col(matrix, indexs):
    for position in indexs:
        for i in range(len(matrix[position[1]])):
            matrix[position[1]][i] = 0

        for j in range(len(matrix)):
            matrix[j][position[0]] = 0
    return matrix


def main():
    indexs = find_position_zero(matrix)
    # print(indexs)
    zero_line_col(matrix, indexs)
    for el in matrix:
        print(*el)


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    main()
