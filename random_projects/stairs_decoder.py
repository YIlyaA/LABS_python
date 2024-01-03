def decode(message_file):
    result = []
    file_lines = []
    with open(message_file, 'r') as f:
        for line in f:
            file_lines.append(line.split())
    file_lines = sorted(file_lines, key=lambda x: int(x[0]))
    numbers = [i for i in range(1, len(file_lines) + 1)]
    stairs_numbers = create_staircase(numbers)
    for el in stairs_numbers:
        for l in file_lines:
            if l[0] == str(el[-1]):
                result.append(l[1])
                break

    return result


def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return []

    return subsets


res = decode(message_file="message_file")
for word in res:
    print(word, end=" ")
