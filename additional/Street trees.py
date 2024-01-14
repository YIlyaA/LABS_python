n = int(input())
numbers = [int(input()) for _ in range(n)]


def minimal_trees_to_plant(n, coordinates):
    if n == 1:
        return 0

    coordinates.sort()  # Sort the coordinates in ascending order
    differences = [coordinates[i + 1] - coordinates[i] for i in range(n - 1)]

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    common_difference = differences[0]
    for diff in differences[1:]:
        common_difference = gcd(common_difference, diff)

    minimal_trees = ((coordinates[-1] - coordinates[0]) // common_difference) + 1
    minimal_trees -= n

    return minimal_trees


print(minimal_trees_to_plant(n, numbers))