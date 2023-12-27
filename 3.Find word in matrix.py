def check_if_one(lst, s, rs):
    if len(lst) == 1:
        if s in lst[0] or rs in lst[0]:
            return "YES"
        else:
            return "NO"
    return "NO"


def check_in_rows(lst, s, rs):
    for line in lst:
        if s in line or rs in line:
            return True
    return False


def check_in_col(lst, s, rs):
    for i in range(m):
        col = ''
        for j in range(n):
            col += lst[j][i]
        if s in col or rs in col:
            return True
    return False


def main():
    if len(lines) == 1:
        print(check_if_one(lines, s, rs))
    elif check_in_rows(lines, s, rs) or check_in_col(lines, s, rs):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = input()
    rs = s[::-1]
    lines = []
    for i in range(n):
        lines.append(input())
    main()