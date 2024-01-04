# 1 way, time-wasting way for a huge amount of numbers

n = int(input())
numbers = list(map(int, input().split()))

count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if abs(numbers[i] - numbers[j]) == 1:
            count += 1

if count == 1:
    print("YES")
else:
    print("NO")

# 2 way - faster way (main solution)
n = int(input())
count = 0
numbers = list(map(int, input().split()))


def find_num(nums):
    nums_set = set(nums)
    for num in nums_set:
        if num + 1 in nums_set or num - 1 in nums_set:
            return "YES"
    return "NO"


print(find_num(numbers))
