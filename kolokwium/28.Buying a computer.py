n = int(input())
models = {}
for _ in range(n):
    dict = {}
    t = list(input().split())
    dict['cpu'] = t[1]
    dict['gpu'] = t[2]
    dict['disc'] = t[3]
    dict['ram'] = t[4]
    dict['price'] = t[5]
    models[t[0]] = dict

m = int(input())
persons = []
for i in range(m):
    dict = {}
    t = list(input().split())
    for el in t:
        dict[el.split(':')[0]] = el.split(':')[1]
    persons.append(dict)
print(models)
print(persons)


for person in persons:
    l = []
    for key_p, value_p in person.items():
        name = =
        for k, dict in models.items():
            num = 0
            for key, value in dict.items():
                if key == key_p:
                    n_num = abs(int(value_p) - int(value))
                    num = min(num, n_num)



