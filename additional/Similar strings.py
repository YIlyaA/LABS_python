s1 = input()
s2 = input()


def similar(s1, s2):
    if s1 == s2:
        return "TAK"
    if abs(len(s1) - len(s2)) >= 2:
        return "NIE"

    if len(s2) < len(s1):
        ns1 = s1[:-1]
        if ns1 == s2:
            return "TAK"
    elif len(s2) > len(s1):
        ns2 = s2[:-1]
        if ns2 == s1:
            return "TAK"

    if len(s2) < len(s1):
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                new_s1 = s1[0:i] + s1[i + 1:]
                if new_s1 == s2:
                    return "TAK"
                else:
                    return "NIE"
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                new_s2 = s2[0:i] + s2[i + 1:]
                if new_s2 == s2:
                    return "TAK"
                else:
                    return "NIE"


print(similar(s1, s2))
