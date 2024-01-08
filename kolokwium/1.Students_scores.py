if __name__ == "__main__":
    n = int(input())
    inf = []
    players = {}
    points = {}
    for i in range(n):
        line = list(map(str, input().split()))
        pl1 = line[0].split(":")[0]
        pl2 = line[1].split(":")[0]
        sc1, sc2 = int(line[0].split(":")[1]), int(line[1].split(":")[1])
        if pl1 not in points:
            points[pl1] = sc1
        else:
            points[pl1] += sc1
        if pl2 not in points:
            points[pl2] = sc2
        else:
            points[pl2] += sc2
        if pl1 not in players:
            players[pl1] = 0
        if pl2 not in players:
            players[pl2] = 0

        if sc1 == sc2:
            continue
        if sc1 > sc2:
            players[pl1] += 1
        else:
            players[pl2] += 1

    new_dict = {}
    for key, value in players.items():
        if value not in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)
    scores = sorted(new_dict, reverse=True)

    res = []
    for score in scores:
        if len(new_dict[score]) > 1:
            l = new_dict[score]
            for i in range(len(l)-1):
                for j in range(i+1, len(l)):
                    if points[l[j]] > points[l[i]]:
                        l[i], l[j] = l[j], l[i]
                    elif points[l[j]] == points[l[i]]:
                        l[i], l[j] = sorted([l[i], l[j]])
            print(l)
            for el in l:
                res.append(el)
        else:
            res.append(new_dict[score][0])
    print(res)
    for name in res:
        print(name)
