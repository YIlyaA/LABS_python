def column_matrix(matrix, n, m):
    col_matrix = []
    for w in range(n):
        t = []
        for k in range(m):
            t.append(matrix[k][w])
        col_matrix.append(sorted(t))
    return col_matrix


def print_sort_col_matrix(cm, n, m):
    for w in range(m):
        for k in range(n):
            print(cm[k][w], end=" ")
        print()


def main():
    col_matrix = column_matrix(matrix, n, m)
    print_sort_col_matrix(col_matrix, n, m)


if __name__ == "__main__":
    matrix = []
    n, m = map(int, input().split())
    for i in range(m):
        matrix.append(list(map(int, input().split())))
    main()