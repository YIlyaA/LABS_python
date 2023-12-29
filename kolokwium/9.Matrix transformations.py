# def reverse_row(x, matrix):
#     matrix[x].reverse()
#     return matrix
#
#
# def matrix_conv(matrix, n, m):
#     new_matrix = []
#     for w in range(n):
#         t = []
#         for k in range(m):
#             t.append(matrix[k][w])
#         new_matrix.append(t)
#     return new_matrix
#
#
# def reverse_column(x, matrix, m, n):
#     matrix_col = matrix_conv(matrix, n, m)
#     matrix_col[x].reverse()
#     new_matrix = matrix_conv(matrix_col, n, m)
#     return new_matrix
#
#
# def main(matrix):
#     for el in opers:
#         if el[0] == "RR":
#             matrix = reverse_row(int(el[1]), matrix)
#         if el[0] == "RC":
#             matrix = reverse_column(int(el[1]), matrix, m, n)
#         if el[0] == "T":
#             matrix = matrix_conv(matrix, n, m)
#
#     for el in matrix:
#         print(*el)
#
#
# if __name__ == "__main__":
#     matrix = []
#     m, n = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(n)]
#     num_of_oper = int(input())
#     opers = [list(input().split()) for _ in range(num_of_oper)]
#     main(matrix)

wiersze,kolumny=[int(x) for x in input().split()]
tablica=[]
for i in range(wiersze):
    linia=[]
    linia=[int(x) for x in input().split()]
    tablica.append(linia)
k=int(input())
dzialania=[]
for i in range(k):
    dzialania.append(input())
for i in range(k):
    dzialanie=dzialania[i].split()
    nazwa=dzialanie[0]
    if(nazwa=='RR'):
        liczba=int(dzialanie[1])
        nowalinia=[]
        for j in range(kolumny):
            nowalinia.append(tablica[liczba][kolumny-j-1])
        tablica[liczba]=nowalinia
    if(nazwa=='RC'):
        liczba=int(dzialanie[1])
        nowalinia=[]
        for j in range(wiersze):
            nowalinia.append(tablica[j][liczba])
        for j in range(wiersze):
            tablica[wiersze-1-j][liczba]=nowalinia[j]
    if(nazwa=='T'):
        h=0
        temp=wiersze
        wiersze=kolumny
        kolumny=temp
        nowatablica=[]
        for i in range(wiersze):
            nowalinia=[]
            for j in range(kolumny):
                nowalinia.append(tablica[j][i])
            nowatablica.append(nowalinia)
        tablica=nowatablica
for i in range(wiersze):
    for j in range(kolumny):
        print(tablica[i][j],end=' ')
    print()