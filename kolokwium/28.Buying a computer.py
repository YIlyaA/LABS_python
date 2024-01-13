# n = int(input())
# models = {}
# for _ in range(n):
#     dict = {}
#     t = list(input().split())
#     dict['cpu'] = t[1]
#     dict['gpu'] = t[2]
#     dict['disc'] = t[3]
#     dict['ram'] = t[4]
#     dict['price'] = t[5]
#     models[t[0]] = dict
#
# m = int(input())
# persons = []
# for i in range(m):
#     dict = {}
#     t = list(input().split())
#     for el in t:
#         dict[el.split(':')[0]] = el.split(':')[1]
#     persons.append(dict)
# print(models)
# print(persons)
#
#
# for person in persons:
#     l = []
#     for key_p, value_p in person.items():
#         name = =
#         for k, dict in models.items():
#             num = 0
#             for key, value in dict.items():
#                 if key == key_p:
#                     n_num = abs(int(value_p) - int(value))
#                     num = min(num, n_num)
#
#
#

n = int(input())
name = []
cpu = []
gpu = []
disc = []
ram = []
price = []
for i in range(n):
    computers = input().split()
    name.append(computers[0])
    cpu.append(computers[1])
    gpu.append(computers[2])
    disc.append(computers[3])
    ram.append(computers[4])
    price.append(computers[5])
customers = int(input())
for i in range(customers):
    expec = input().split()
    computer = []
    for g in range(n):
        computer.append(1)
    for j in expec:
        line = j.split(":")
        if (line[0] == 'gpu'):
            for h in range(n):
                if (computer[h] != 0):
                    if (int(line[1]) <= int(gpu[h])):
                        computer[h] = 1
                    else:
                        computer[h] = 0
        if (line[0] == 'cpu'):
            for h in range(n):
                if (computer[h] != 0):
                    if (int(line[1]) <= int(cpu[h])):
                        computer[h] = 1
                    else:
                        computer[h] = 0
        if (line[0] == 'disc'):
            for h in range(n):
                if (computer[h] != 0):
                    if (int(line[1]) <= int(disc[h])):
                        computer[h] = 1
                    else:
                        computer[h] = 0
        if (line[0] == 'ram'):
            for h in range(n):
                if (computer[h] != 0):
                    if (int(line[1]) <= int(ram[h])):
                        computer[h] = 1
                    else:
                        computer[h] = 0
    possible = []
    for z in range(n):
        if (computer[z] == 1):
            line = [name[z], int(price[z])]
            possible.append(line)
    possible.sort(key=lambda x: x[0])
    possible.sort(key=lambda x: x[1])
    print(possible[0][0])
