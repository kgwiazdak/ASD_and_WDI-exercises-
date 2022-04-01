def waga(number):
    odwazniki = [1,2,5,9]
    zwrot = []
    def rek(odwazniki, number, cur=0, index = 0, tablica1=[], tablica2=[]):
        nonlocal zwrot
        if cur==number:
            zwrot.append((tablica1, tablica2))
            return True
        if index==len(odwazniki):
            return False
        return rek(odwazniki, number, cur, index+1, tablica1, tablica2) | rek(odwazniki, number, cur+odwazniki[index], index+1, tablica1.append(odwazniki[index]), tablica2) | rek(odwazniki, number+odwazniki[index], cur, index+1, tablica1, tablica2.append(odwazniki[index]))
    rek(odwazniki, number)
    return zwrot




