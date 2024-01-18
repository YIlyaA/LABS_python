# n = int(input())
# strings = [input() for _ in range(n)]
#
#
# def is_substring(small, big):
#     for i in range(len(small)):
#         word = small[:i] + small[i + 1:]
#         if word in big and len(big) % len(word) == 0 and len(big) // len(word) >= 2:
#             return True
#     return False
#
#
# counter = 0
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if len(strings[j]) == len(strings[i]):
#             continue
#         if len(strings[j]) % len(strings[i]) == 0:
#             if strings[j][:len(strings[i])] == strings[i]:
#                 counter += 1
#         if len(strings[i]) % len(strings[j]) == 0:
#             if strings[i][:len(strings[j])] == strings[j]:
#                 counter += 1
#         if len(strings[i]) > len(strings[j]):
#             if is_substring(strings[j], strings[i]):
#                 counter += 1
#         if len(strings[i]) < len(strings[j]):
#             if is_substring(strings[i], strings[j]):
#                 counter += 1
# print(counter)

N = int(input())
stringi = [input() for _ in range(N)]
counter = 0

for x in range(N-1):
    tested = stringi[x]
    for gg in range(x+1, N):
        if len(tested) == len(stringi[gg]):
            continue
        if len(tested) < len(stringi[gg]):
            gggg = stringi[gg]
            for z in range(len(tested)):
                dupa = 0
                test = tested[:z] + tested[z + 1:]
                if len(stringi[gg]) % len(test) == 0:
                    a = int(len(stringi[gg]) / len(test))
                    if test * a == stringi[gg]:
                        dupa += 1
                if dupa == 1:
                    counter += 1
                    break

print(counter)
