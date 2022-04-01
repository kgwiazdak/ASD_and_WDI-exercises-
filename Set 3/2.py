def exe2(tablica):
    def w_weight(liczba):
        counter = 0
        last = 0
        i=2
        while liczba!=1:
            while liczba%i==0:
                liczba//=i
                last = i
            if last==i:  counter+=1
            i+=1
        return counter
    def arr_transformation(tablica):
        blok = [0 for _ in range(len(tablica))]
        for i in range(len(tablica)):
            waga = w_weight(tablica[i])
            blok[i] = waga
        return blok

    nowa_tablica = arr_transformation(tablica)
    print(nowa_tablica)
    table = []

    def podzial(tablica, table, l=0,s=0,p=0, n=0):
        if n==len(tablica):
            if l==p==s:
                table.append(1)
                return True
            else:return False

        return podzial(tablica,table, l+tablca[n], s, p, n+1) | podzial(tablica,table, l, s+tablca[n], p, n+1) | podzial(tablica,table, l, s, p+tablca[n], n+1)


    podzial(nowa_tablica, table)
    print(table)
    if table:
        return True
    return False


if __name__ == '__main__':
    from random import randint
    #tablca = [randint(1, 1000)for i in range(10)]
    tablca = [6,18,24]
    print(tablca)
    print(exe2(tablca))
