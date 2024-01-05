n = input()
num = []
count = 0
for i in range(len(n)):
    k = 0
    for j in range(len(n) - i):
        word = ""
        for h in range(k, k + i + 1):
            word = word + n[h]
        k = k + 1
        num.append(word)


def is_palindrom(word):
    if word[0] == '0':
        return False
    for i in range(len(word) - 1, 0, -1):
        new_word = ""
        if word[i] == "0":
            for j in range(len(word) - 1):
                new_word = new_word + word[j]
            word = new_word
        else:
            return word == word[::-1]
    return word == word[::-1]


for el in num:
    if is_palindrom(el) == True:
        count = count + 1
print(count)
