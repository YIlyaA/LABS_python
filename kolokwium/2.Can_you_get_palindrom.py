string = input().lower()


def check_palindrom(s):
    rev_str = s[::-1]
    if rev_str == s:
        return "YES"

    l = len(s) // 2
    counter_mistake = 0
    d = 0
    for i in range(int(len(s) / 2)):
        if s[i] != s[-i - 1]:
            # print(s[i], s[-i-1])
            new_s1 = s[:i] + s[i + 1:]
            ind = len(s) - i - 1
            new_s2 = s[:ind] + s[ind + 1:]

            if new_s1[i] == new_s1[-i] or new_s1[i - 1] == new_s1[-i + 1]:
                s = new_s1
                d += 1
                # print(new_s1)
                # print(f"s={s}")
            elif new_s2[i] == new_s2[-i] or new_s2[i - 1] == new_s2[-i + 1]:
                s = new_s2
                d += 1
                # print(new_s2)
                # print(f"s={s}")
            else:
                counter_mistake += 1
            #     print(f"s={s}")
            # print(f"----------------- {counter_mistake}, {d} --------------------")

    if counter_mistake + d <= 2:
        return "YES"
    else:
        return "NO"


print(check_palindrom(string))
