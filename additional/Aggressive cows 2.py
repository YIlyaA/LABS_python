def is_valid(mid, cows, stalls):
    count = 1
    last_position = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= mid:
            count += 1
            last_position = stalls[i]

    return count >= cows


def largest_minimum_distance(n, cows, stalls):
    stalls.sort()

    low, high = 1, stalls[-1] - stalls[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2

        if is_valid(mid, cows, stalls):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


# Sample Input
n, c = map(int, input().split())
stalls = [int(input()) for _ in range(n)]

# Sample Output
result = largest_minimum_distance(n, c, stalls)
print(result)
