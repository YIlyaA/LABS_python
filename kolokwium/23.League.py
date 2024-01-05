def check_wins(dict, games):
    for game in games:
        dict[game[0]][1] -= 1  # games can to play
        dict[game[1]][1] -= 1  #
        if int(game[-2]) > int(game[-1]):
            dict[game[0]][0] += 1  # wins
        else:
            dict[game[1]][0] += 1  # wins

    return dict


def check_results(res, t):
    answer = []
    for key, value in res.items():
        if sum(value) >= t:
            answer.append(key)
    return answer


N, M, T = map(int, input().split())
teams = {}
for _ in range(N):
    teams[input()] = [0, N-1]
games = [input().split(':') for _ in range(M)]

res_dict = check_wins(teams, games)
ans = check_results(res_dict, T)
ans.sort()
for el in ans:
    print(el)

