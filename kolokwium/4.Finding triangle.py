n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
square = []

for i in range(n-2):
    px1, py1 = points[i][0], points[i][1]
    for j in range(i+1, n-1):
        px2, py2 = points[j][0], points[j][1]
        for k in range(j+1, n):
            px3, py3 = points[k][0], points[k][1]

            x1, y1 = px2 - px1, py2 - py1
            x2, y2 = px3 - px1, py3 - py1

            s = abs(x1*y2 - y1*x2)/2
            if s == 0:
                continue
            else:
                square.append(s)

print(min(square), max(square))
