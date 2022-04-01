def czynniki_pierwsze(number):
    tablica = []
    from math import sqrt
    for i in range(3, int(sqrt(number)), 2):
        if number%i==0:
            tablica.append(i)
    if number%2==0:
        tablica.append(2)
    return tablica


def zadanie31(number):
    tablica = czynniki_pierwsze(number)
    liczba = 0
    def rek(tablica, index=0, number=1, poprzedni_number=1):
        nonlocal liczba
        if number!=poprzedni_number:
            if number!=1:
                liczba+=number
            if 1 in tablica:
                liczba+=1
        if index==len(tablica):
            return False
        if index!=len(tablica)-1:
            return rek(tablica, index+1, number, number) | rek(tablica, index+1, number*tablica[index], number)
        else:
            return rek(tablica,index+1,number*tablica[index])
    rek(tablica)
    return liczba
