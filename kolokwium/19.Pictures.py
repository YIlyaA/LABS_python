H, W, Y, X = [int(x) for x in input().split()]
wall = [list(map(int, input().split())) for _ in range(H)]

flag = False
for i in range(0, H - Y + 1):
    for j in range(0, W - X + 1):
        flag2 = True
        for h in range(i, Y + i):
            for k in range(j, X + j):
                if wall[h][k] != 0:
                    flag2 = False
        if flag2:
            flag = True
print(flag)
