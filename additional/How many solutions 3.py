# -------------Not efficient solution-------------
def count_integer_solutions(n, x, y):
    count = 0
    for a in range(n + 1):
        for b in range(n + 1):
            for c in range(n + 1):
                for d in range(n + 1):
                    if x * a**2 + y * b**2 == x * c**2 + y * d**2:
                        count += 1
    return count

n, x, y = map(int, input().split())

result = count_integer_solutions(n, x, y)
print(result)

