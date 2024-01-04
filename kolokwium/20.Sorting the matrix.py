n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

sort_matrix = []
for el in matrix:
    sort_matrix.extend(el)
sort_matrix = sorted(sort_matrix)

mt = []
for i in range(m):
    t = []
    for j in range(n):
        t.append(sort_matrix[j])
    mt.append(t)
    sort_matrix = sort_matrix[n:]

cm = []
for i in range(n):
    tt = []
    for j in range(m):
        tt.append(mt[j][i])
    cm.append(tt)

for el in cm:
    print(*el)