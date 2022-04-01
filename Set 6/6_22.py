def czynnik_pierwszy(number):
    tablica = []
    from math import sqrt
    for i in range(3, int(sqrt(number)), 2):
        if number%i==0:
            tablica.append(i)
    if number%2==0:
        tablica.append(2)
    return tablica


def zadanie22(T, index=0, counter=0):
    if index==len(T):
        return counter
    tablica = czynnik_pierwszy(T[index])
    for i in tablica:
        if index+i<=len(T):
            return zadanie22(T, index+i, counter+1)
    return -1

