def chess(tablica, kolumna):

    nowa = []

    def suma(tablica, kolumna, nowa, wiersz = 0, costs=0):
        costs += tablica[wiersz][kolumna]
        if wiersz == 7:
            if costs not in nowa:
                nowa.append(costs)
            return True

        if kolumna==0:
            return suma(tablica,kolumna,nowa,wiersz+1,costs) | suma(tablica,kolumna+1,nowa,wiersz+1,costs)
        elif kolumna==7:
            return suma(tablica,kolumna,nowa,wiersz+1,costs) | suma(tablica,kolumna-1,nowa,wiersz+1,costs)
        else:
            return suma(tablica,kolumna,nowa,wiersz+1,costs) | suma(tablica,kolumna+1,nowa,wiersz+1,costs) | suma(tablica,kolumna-1,nowa,wiersz+1,costs)

    suma(tablica,kolumna,nowa)
    nowa.sort()
    return nowa[0]

if __name__ == '__main__':
    from random import randint
    tablica = [[randint(1, 100)for _ in range(8)]for _ in range(8)]
    for element in tablica:
        print(element)
    print()
    kolumna = int(input('Wpisz kolumnę w której stoi król (1-8): '))
    print(chess(tablica, kolumna - 1))
