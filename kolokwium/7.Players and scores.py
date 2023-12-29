def sort_set(pl, eq_index):
    new_list = []
    for el in eq_index:
        new_list.append((pl[el][0], pl[el][1]))
    ll = sorted(new_list)
    j = 0
    for i in eq_index:
        # print("-------------- before op --------------", pl)
        pl.pop(i)
        # print(f"remove el: {i}", pl)
        pl.insert(i, ll[j])
        # print(f"add el {i}", pl)
        j += 1
    return pl

def ind_eq(arr):
    n=len(arr)
    res=[]
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i][1]==arr[j][1]:
                if i not in res:
                    res.append(i)
                elif j not in res:
                    res.append(j)
    return sorted(res)

def check_winner(games):
    winners = {}
    for game in games:
        names = []
        points = []
        for i in range(len(game)):
            res = game[i].split(":")
            names.append(res[0])
            points.append(int(res[1]))

        if points[0] == points[1]:
            new = sorted(names)
            for i in range(0, 2):
                if new[i] in winners:
                    if winners[new[i]] < points[i]:
                        winners[new[i]] = points[i]
                else:
                    winners[new[i]] = points[i]
        else:
            for i in range(0, 2):
                if names[i] in winners:
                    if winners[names[i]] < points[i]:
                        winners[names[i]] = points[i]
                else:
                    winners[names[i]] = points[i]

    return winners


def sort_players_points(pl):
    sort_list = sorted(pl.items(), key=lambda item: item[1], reverse=True)
    return sort_list


def main():
    players = check_winner(games)
    sort_pl = sort_players_points(players)
    # print(sort_pl)
    indexs = ind_eq(sort_pl)
    # print(indexs)
    if len(indexs) >= 1:
        s_pl = sort_set(sort_pl, indexs)
        for key in s_pl:
            print(key[0])
    else:
        for key in sort_pl:
            print(key[0])


if __name__ == "__main__":
    n = int(input())
    games = [list(input().split()) for _ in range(n)]
    main()