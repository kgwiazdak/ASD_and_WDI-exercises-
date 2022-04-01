def enki(T, number):
    licznik = 0
    zwrot = []
    def rek(T, number, cur=1, index=0, tablica = []):
        nonlocal licznik, zwrot
        if number==cur:
            licznik+=1
            zwrot.append(tablica)
            return True
        if index==len(T) or number<cur or cur==0:
            return False
        return rek(T, number, cur, index+1, tablica) | rek(T, number, cur*T[index], index+1, tablica.append(T[index]))
    rek(T, number)
    return licznik, zwrot


