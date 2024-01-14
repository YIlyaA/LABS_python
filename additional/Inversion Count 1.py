def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inversions = count_inversions(arr[:mid])
    right, right_inversions = count_inversions(arr[mid:])

    merged, split_inversions = merge_and_count(left, right)

    total_inversions = left_inversions + right_inversions + split_inversions

    return merged, total_inversions


def merge_and_count(left, right):
    merged = []
    split_inversions = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inversions += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, split_inversions


# Input
n = int(input())
arr = [int(input()) for _ in range(n)]

# Count inversions
sorted_arr, inversions = count_inversions(arr)

# Output
print(inversions)
