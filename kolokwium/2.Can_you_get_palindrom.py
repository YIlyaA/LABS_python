string = input().lower()


def check_palindrom(s):
    rev_str = s[::-1]
    if rev_str == s:
        return "YES"

    l = len(s) // 2
    counter_mistake = 0
    for i in range(int(len(s) / 2)):
        if s[i] != s[-i - 1]:
            counter_mistake += 1
            print(f'--- {s[i]} and {s[-i - 1]}, {counter_mistake}---')

    if counter_mistake <= 2:
        return "YES"
    else:
        return "NO"


print(check_palindrom(string))
