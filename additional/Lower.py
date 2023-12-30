n = int(input())
squares = list(map(int, input().split()))

counter = 0
max_counter = 0
for i in range(n-1):
    if squares[i+1] <= squares[i]:
        counter += 1
        max_counter = max(max_counter, counter)
    else:
        counter = 0
print(max_counter)
