s = input().split()
n = int(s[0])
k = int(s[1])
start = []


def print_sequence_to_zero(start, n, k):
    start.append(n)
    if n > 0:
        print_sequence_to_zero(start, n - k, k)
    return set(start)


def print_sequence_from_zero(start, n, k):
    start.append(n)
    if n == start[0]:
        return start
    else:
        return print_sequence_from_zero(start, n + k, k)


start = print_sequence_to_zero(start, n, k)
start = list(start)
n = start[-1]
start = start[:-1]
sequence = print_sequence_from_zero(start, n, k)
print(*sequence)
