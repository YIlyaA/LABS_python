n, s = map(int, input().split())
students = [list(input().split()) for _ in range(n)]
k = int(input())
tests = [list(input().split()) for _ in range(k)]


def mark_to(key, value, s):
    while len(value) != s:
        value.append(0)
    avg_sum = sum(value) / s
    if 0 <= avg_sum < 2:
        return [key, 2]
    if 3 <= avg_sum < 3.5:
        return [key, 3]
    if 3.5 <= avg_sum < 4.5:
        return [key, 4]
    if 4.5 <= avg_sum <= 5:
        return [key, 5]


res = {}
for el in students:
    nam = el[0]
    res[nam] = []
print(tests)
for test in tests:
    name = test[0]
    if 'inf' in name:
        name = name[3:]
    score = int(test[-1].split("/")[0])
    max_score = int(test[-1].split("/")[1])

    for student in students:
        if name in student:
            x = score / max_score * 100
            if x < 50:
                mark = 2
            elif 50 <= x < 70:
                mark = 3
            elif 70 <= x < 90:
                mark = 4
            else:
                mark = 5
            res[student[0]].append(mark)

result = []
for key, value in res.items():
    result.append(mark_to(key, value, s))
print(result)
result = sorted(result)
for k in result:
    print(*k)
