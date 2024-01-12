# Magic Word is a string in which each letter is strictly greater than the previous one (according to ASCII,
# i.e 'a' > 'Z') (one letter strings are  Magic Words). You are given a string S composed of letters of english
# alphabet. (len(S) < 30) How many substrings (contiguous sequence of characters within a string) of S are Magic
# Words? (print this value)
s = input()
substr = []
for i in range(1, len(s)):
    sub = []
    count = 0
    for j in range(len(s) - i):
        word = ''
        for k in range(count, count + i + 1):
            word += s[k]
        sub.append(word)
        count += 1
    substr.append(sub)

counter = len(s)


def magic_word(sub_list):
    count = 0
    for el in sub_list:
        for letters in el:
            t = []
            for letter in letters:
                t.append(ord(letter))
            test = 0
            for i in range(len(t) - 1):
                if t[i] < t[i + 1]:
                    test += 1
            if test == len(t) - 1:
                count += 1
    return count


print(counter + magic_word(substr))
