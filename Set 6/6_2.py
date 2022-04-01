def how_many_prime(number):
    if number==2 or number==3:
        return 1
    if number<2:
        return 0
    from math import sqrt
    counter = 0
    for i in range(3,int(sqrt(number)), 2):
        if number%i==0:
            counter+=1
    if number%2==0:
        counter+=1
    return counter

def waga(T):
    tablica=[]
    for element in T:
        a = how_many_prime(element)
        tablica.append(a)

    def rek(tablica, index=0, A=0, B=0, C=0):
        if index==len(tablica):
            if A==B==C:     return True
            else:           return False
        return rek(tablica, index+1, A+tablica[index], B, C) | rek(tablica, index+1, A, B+tablica[index], C) | rek(tablica, index+1, A, B, C+tablica[index])

    return rek(T)


