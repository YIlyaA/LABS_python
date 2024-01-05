numbers = map(int, input().split())


def max_contiguous_sum(arr):
    max_sum = 0
    current_sum = 0

    for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


result = max_contiguous_sum(numbers)
print(result)
