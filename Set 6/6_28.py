def ile_jedynek(number):
    liczba = 1
    counter = 0
    while number!=0:
        if number//2==0:
            number//=2
            liczba*=10
            counter+=1
        else:
            number-=1
            number//=2
            liczba=liczba*10+1
            counter+=1
    new = 1
    liczba//=10
    while liczba!=0:
        if liczba%10==0:
            new*=10
            liczba//=10
        else:
            new*=10
            new+=1
            liczba//=10
    new//=10

    licznik = 0
    while new!=0:
        if new%10==0:
            new//=10
        else:
            licznik+=1
            new-=1
            new//=10
    return licznik

def zadanie28(T):
    tablica = []
    for element in T:
        tablica.append(ile_jedynek(element))
    print(tablica)

    def rek(tablica,index=0, jeden=0, drugi=0, trzeci=0):
        if jeden==drugi==trzeci!=0:
            return True
        if index==len(tablica):
            return False
        return rek(tablica, index+1, jeden, drugi,trzeci) | rek(tablica, index+1, jeden+tablica[index], drugi, trzeci) | rek(tablica, index+1, jeden, drugi+tablica[index],trzeci) | rek(tablica, index+1, jeden, drugi,trzeci+tablica[index])

    return rek(tablica)


