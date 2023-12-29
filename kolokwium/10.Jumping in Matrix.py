# def check_the_smallest(matrix_r, matrix_c, x, y):
#     x1 = y1 = matrix_r[x][y]
#
#     xx = min(matrix_r[x])
#     index_x = matrix_r[x].index(xx)
#     yy = min(matrix_c[index_x])
#     index_y = matrix_c[index_x].index(yy)
#     while xx != yy:
#         xx = min(matrix_r[index_y])
#         index_x = matrix_r[index_y].index(xx)
#         yy = min(matrix_c[index_x])
#         index_y = matrix_c[index_x].index(yy)
#     rix = matrix_r[index_y].index(xx)
#     riy = matrix_c[index_x].index(yy)
#
#     return [rix, riy]
#
#
# def row_to_column(matrix_r):
#     matrix_c = []
#     for i in range(len(matrix_r)):
#         time = []
#         for j in range(len(matrix_r)):
#             time.append(matrix_r[j][i])
#         matrix_c.append(time)
#     return matrix_c
#
#
# def main():
#     matrix_column = row_to_column(matrix_row)
#     print(*check_the_smallest(matrix_row, matrix_column, x, y))
#
#
# if __name__ == "__main__":
#     matrix_row = []
#     n = int(input())
#     x, y = map(int, input().split())
#     for i in range(n):
#         matrix_row.append(list(map(int, input().split())))
#     main()

n=int(input())
pozycjai,pozycjaj=[int(x) for x in input().split()]
wiersze=[]
for i in range(n):
    linia=[int(x) for x in input().split()]
    wiersze.append(linia)
kolumny=[]
for i in range(n):
    kolumna=[]
    for j in range(n):
        kolumna.append(wiersze[j][i])
    kolumny.append(kolumna)
poczatek=wiersze[pozycjai][pozycjaj]
for i in range(n):
    if(i%2==0):
        nastepny=min(wiersze[pozycjai])
        for j in range(n):
            if(wiersze[pozycjai][j]==nastepny):
                pozycjaj=j
                break
    else:
        nastepny=min(kolumny[pozycjaj])
        for j in range(n):
            if(kolumny[pozycjaj][j]==nastepny):
                pozycjai=j
                break
print(pozycjai, pozycjaj)