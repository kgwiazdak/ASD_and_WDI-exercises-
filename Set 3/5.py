bolek = False

def prime(number):
    from math import sqrt
    if number==2 or number==3 or number==5 or number==7:
        return True
    if number%2==0 or number%3==0 or number%5==0 or number<2:
        return False
    for i in range(3, int(sqrt(number)), 2):
        if number%i==0:
            return False
    return True


def exe4(tablica, n=1):
    if n==len(tablica):
        for element in tablica:
            if prime(element) ==False:
                return False
            return True
    nowa = tablica.copy()
    nowa[n-1] = tablica[n-1]*10+tablica[n]
    del nowa[n]
    return exe4(tablica, n + 1) | exe4(nowa, n)



if __name__ == '__main__':
    from random import randint
    tablica = [randint(0,1)for _ in range(6)]
    exe4(tablica)
    print(bolek)

