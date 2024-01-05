import math

n = int(input())
numbers = [int(input()) for _ in range(n)]


def is_prime(num):
    if num < 2:
        return "NO"
    if num % 2 == 0:
        return "NO"
    else:
        for i in range(3, math.isqrt(num)+1, 2):
            if num % i == 0:
                return "NO"
        return "YES"


for number in numbers:
    print(is_prime(number))
