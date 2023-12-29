def average_score_ind(line):
    # counting the average score of student
    line.pop(0)
    count = 0
    score_sum = 0
    for el in line:
        s = el.split(":")
        score_sum += float(s[1])
        count += 1
    return score_sum / count


def average_score_ex(list):
    for line in list:
        for i in line:
            counter = 0
            s = i.split(":")
            letter = s[0]
            number = float(s[1])
            if len(dict) != 0:
                for key, value in dict.items():
                    if key == letter:
                        dict[key] = value + number
                        counter += 1
            else:
                dict[letter] = float(number)
            if counter == 0:
                dict[letter] = float(number)
    return dict


def counting_letters(ll):
    letters = []
    count = 0
    for line in ll:
        for i in line:
            s = i.split(":")
            letters.append(s[0])
    letters.sort()
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def division_dict(dict1, dict2):
    result_dict = {}
    for key in dict1:
        if key in dict2:
            result_dict[key] = dict1[key] / dict2[key]
    return result_dict


def main():
    for line in inf:
        print(line[0], average_score_ind(line))
    dict1 = average_score_ex(inf)
    dict2 = counting_letters(inf)
    dict = division_dict(dict1=dict1, dict2=dict2)
    dd = sorted(dict.items())
    for key, value in dd:
        print(key, value)


if __name__ == "__main__":
    number_students = int(input())
    inf = []
    dict = {}
    for i in range(number_students):
        line = list(map(str, input().split()))
        inf.append(line)
    inf = sorted(inf)
    main()