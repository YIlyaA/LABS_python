def check_digits(field):
    for el in field:
        if not check_for_uniq(el):
            return False
    return True


def field_to_col(field_row):
    field_col = []
    for i in range(len(field_row)):
        t = []
        for j in range(len(field_row)):
            t.append(field_row[j][i])
        field_col.append(t)
    return field_col


def check_diag(field_row):
    diag1 = [field_row[i][i] for i in range(len(field_row))]
    diag2 = [field_row[i][-i - 1] for i in range(len(field_row))]
    if check_for_uniq(diag1) and check_for_uniq(diag2):
        return True
    return False


def check_for_uniq(s):
    setarr = set(s)
    if len(setarr) == len(s):
        return True
    return False


def main():
    field_row = []
    for i in range(9):
        field_row.append(list(map(int, input().split())))
    field_col = field_to_col(field_row)
    if check_digits(field_row) and check_digits(field_col):
        if check_diag(field_row):
            print("X")
        else:
            print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()