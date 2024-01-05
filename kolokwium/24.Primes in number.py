num = input()
numbers = []

for i in range(len(num)):
    k = 0
    for j in range(len(num) - i):
        w = ''
        for h in range(k, k + i + 1):
            w += num[h]
        numbers.append(int(w))
        k += 1


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


numbers = set(numbers)
primes = []
for l in numbers:
    if is_prime(l):
        primes.append(str(l))

primes.sort(reverse=True)

for el in primes:
    print(el)
