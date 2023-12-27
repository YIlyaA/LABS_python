def oper_go(opers, s):
    comp_str = s
    new_str = s
    for oper in opers:
        fr = min(int(oper[0]), int(oper[1]))
        to = max(int(oper[0]), int(oper[1]))
        new_str = new_str[0:fr] + oper[2] + new_str[to + 1:]
        if len(new_str) > len(comp_str):
            comp_str = new_str
    return [new_str, comp_str]


def main():
    strings = oper_go(operations, string)
    for s in strings:
        print(s)


if __name__ == "__main__":
    n, m = map(int, input().split())
    string = input()
    operations = []
    for _ in range(m):
        operations.append(list(input().split(";")))
    main()