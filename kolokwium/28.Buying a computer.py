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
persons = {}
for i in range(m):
    dict = {}
    t = list(input().split())
    for el in t:
        dict[el.split(':')[0]] = el.split(':')[1]
    persons[i] = dict
print(models)
print(persons)
