n = int(input())
numbers = [int(x) for x in input().split()]

lists = []
for i in range(0, n + 1):
    for j in range(i + 1, n + 1):
        new_list = numbers[i:j]
        lists.append(new_list)

sum_A = []
sum_B = []

for el in lists:
    suma = 0
    for i in range(len(el)):
        if i % 2 == 0:
            suma = suma + el[i]
    sum_A.append(suma)
for el in lists:
    suma = 0
    for i in range(len(el)):
        if i % 3 == 0:
            suma = suma + el[i]
    sum_B.append(suma)

eq_sum = []
for a in sum_A:
    for b in sum_B:
        if a == b:
            eq_sum.append(a)

print(max(eq_sum))
