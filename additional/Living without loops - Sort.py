# Given a sequence of numbers, sort them and output in nondecreasing order.
# However, to make it more interesting you cannot use in your code the following:
# for, while, sum, map, reduce, exec, compile, eval, sort, single, import, filter
# input: 8 7 6 5
# output: 5 6 7 8

s = input().split()


def sorting(s, i=0, swapped=False):
    if i == len(s) - 1:
        if swapped:
            return sorting(s, 0, False)
        else:
            return s
    if int(s[i]) > int(s[i + 1]):
        s[i], s[i + 1] = s[i + 1], s[i]
        return sorting(s, i + 1, True)
    else:
        return sorting(s, i + 1, swapped)


print(" ".join(sorting(s)))
