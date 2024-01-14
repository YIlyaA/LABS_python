import sys

szachy = []
ii = []
jj = []
pozycjei = []
pozycjej = []
for i in range(8):
    szachy.append(input())
for i in range(8):
    for j in range(8):
        if (szachy[i][j] == 'k'):
            kingi = i
            kingj = j
            pozycjei.append(kingi)
            pozycjej.append(kingj)
        if (szachy[i][j] == 'w'):
            ii.append(i)
            jj.append(j)
noweii = ii
nowejj = jj
if (kingi in ii or kingj in jj):
    # mat or game goes on
    if (kingi - 1 >= 0): pozycjei.append(kingi - 1)
    if (kingi + 1 < 8): pozycjei.append(kingi + 1)
    if (kingj - 1 >= 0): pozycjej.append(kingj - 1)
    if (kingj + 1 < 8): pozycjej.append(kingj + 1)
    for eli in pozycjei:
        for elj in pozycjej:
            if (szachy[eli][elj] == 'w'):
                for h in range(len(noweii)):
                    if (noweii[h] == eli):
                        del noweii[h]
                        break
                for h in range(len(nowejj)):
                    if (nowejj[h] == elj):
                        del nowejj[h]
                        break
            if (eli in noweii or elj in nowejj):
                noweii = ii
                nowejj = jj
            else:
                print("game goes on")
                sys.exit()
    print("mat")
else:
    # pat or game goes on
    if (kingi - 1 >= 0): pozycjei.append(kingi - 1)
    if (kingi + 1 < 8): pozycjei.append(kingi + 1)
    if (kingj - 1 >= 0): pozycjej.append(kingj - 1)
    if (kingj + 1 < 8): pozycjej.append(kingj + 1)
    for eli in pozycjei:
        for elj in pozycjej:
            if (eli == kingi and elj == kingj): break
            if (szachy[eli][elj] == 'w'):
                for h in range(len(noweii)):
                    if (noweii[h] == eli):
                        del noweii[h]
                        break
                for h in range(len(nowejj)):
                    if (nowejj[h] == elj):
                        del nowejj[h]
                        break
            if (eli in noweii or elj in nowejj):
                noweii = ii
                nowejj = jj
            else:
                print("game goes on")
                sys.exit()
    print("pat")
