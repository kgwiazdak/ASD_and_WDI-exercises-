from math import sqrt
suma = 0

def prime(number):
    tablica = []

    if number%2==0:
        tablica.append(2)

    for i in range(3, int(sqrt(number))+2,2):
        if number%i==0:
            tablica.append(i)
    return tablica

def exe30(number):
    dzielniki = prime(number)

    def rek(dzielniki,indeks=0, ktory = 1):
        global suma

        if indeks == len(dzielniki):
            suma+=ktory
            return True

        return rek(dzielniki, indeks+1, ktory*dzielniki[indeks]) | rek(dzielniki, indeks+1, ktory)
    rek(dzielniki)


if __name__ == '__main__':
   exe30(60)
   print(suma)

