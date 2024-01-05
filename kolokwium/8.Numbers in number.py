number = input()

length_num = []

for i in range(len(number)):
    numbers = []
    count = 0
    for j in range(len(number) - i):
        word = ''
        for k in range(count, count + i + 1):
            word += number[k]
        numbers.append(word)
        count += 1
    length_num.append(numbers)


def occurs_times(num):
    dict = {}
    list_max = []
    for el in num:
        if el in dict:
            dict[el] += 1
        else:
            dict[el] = 1
    max_val = max(dict.values())
    for key, value in dict.items():
        if value == max_val:
            list_max.append(int(key))
    min_val = min(list_max)
    return str(min_val)


for el in length_num:
    print(occurs_times(el))
