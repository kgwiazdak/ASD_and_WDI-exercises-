p = [2,3,5,7]
from math import sqrt

def prime():
    global p
    for number in range(7,500,2):
        if number%2==0 or number%3==0 or number%5==0 or number<2:
            continue

        for i in range(3, int(sqrt(number)+1),2):
            if number%i==0:
                break
        p.append(number)

def exe22(tablica, indeks=0, counter=0):
    if indeks == len(tablica)-1:
        print(counter)
        exit()

    global p



    for i in p:
        if i>int(sqrt(tablica[indeks])):
            break
        if tablica[indeks]%i==0:
            if indeks+i<len(tablica):
                nowy = indeks+i
                exe22(tablica, nowy, counter + 1)



if __name__ == '__main__':
    from random import randint
    n = 20
    tablica = [randint(1,500)for _ in range(n)]
    print(tablica)
    print()
    prime()
    exe22(tablica)
