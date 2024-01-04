s1 = input()
s2 = input()


def similar(s1, s2):
    error = 0
    if s1 == s2:
        return "TAK"
    if len(s1) - 1 != len(s2):
        return "NIE"
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            s1_new = s1[:i] + s1[i + 1:]
            error += 1
            if s1_new == s2:
                return "TAK"
    if error > 1:
        return "NIE"
    else:
        return "TAK"


print(similar(s1, s2))
