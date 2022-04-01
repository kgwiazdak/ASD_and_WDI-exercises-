def hetman(n):
    tablica = [-1 for _ in range(n)]
    t0 = [False for _ in range(n)]
    t1 = t2 = [False for _ in range(n*2-1)]

    def queen(wiersz, kolumna):
        if wiersz==n:
            print(tablica)
            exit()
        else:
            if (t0[kolumna] or t1[wiersz+kolumna] or t2[n-1+wiersz-kolumna]):
                return

            tablica[wiersz] = kolumna
            t0[kolumna] = t1[wiersz+kolumna] = t2[n-1+wiersz-kolumna] = True

            for i in range(n):
                queen(wiersz+1, i)
            t0[kolumna] = t1[wiersz + kolumna] = t2[n -1+ wiersz - kolumna] = False


    for i in range(n):
        queen(0, i)

print(hetman(4))
