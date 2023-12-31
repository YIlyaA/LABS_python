def distance(c1, c2, nc):
    x1, y1, x2, y2 = 0, 0, 0, 0
    for el in nc:
        if c1 == el[0]:
            x1, y1 = float(el[-2]), float(el[-1])
        if c2 == el[0]:
            x2, y2 = float(el[-2]), float(el[-1])
    dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5
    print("DIS: ", dis)
    return dis


n = int(input())
name_city = [input().split() for _ in range(n)]
order = input().split()
order.append(order[0])

numbers = 0
for city in range(len(order) - 1):
    c1 = order[city]
    c2 = order[city + 1]
    numbers += distance(c1, c2, name_city)

print(round(numbers, 3))
