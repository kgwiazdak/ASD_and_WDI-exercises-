def czy_pierwsza(number):
    if number%2==0 or number%3==0 or number<2:
        return False
    from math import sqrt
    for i in range(3, int(sqrt(number)), 2):
        if number%i==0:
            return False
    return True

def dec2bin(number):
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
    return new

def bin2dec(number):
    counter = 0
    liczba = number
    while liczba!=0:
        liczba//=10
        counter+=1
    new = 0
    i=0
    while number!=0:
        ostatnia = number%10
        new+=(ostatnia*2**i)
        i+=1
        number//=10
    return new

def zadanie26(jedynki, zera):
    counter = 0
    def rek(jedynki, zera, n=1):
        if jedynki==zera==0:
            nonlocal counter
            if not czy_pierwsza(bin2dec(n)):
                counter+=1
                print(n)
            return True
        if jedynki!=0:
            n1=n*10+1
            if zera!=0:
                n0=n*10
                return rek(jedynki-1, zera, n1) | rek(jedynki, zera-1, n0)
            else:
                return rek(jedynki-1, zera, n1)
        if zera!=0 and jedynki==0:
            n0=n*10
            return rek(jedynki, zera-1, n0)
    rek(jedynki-1, zera)
    return counter

if __name__ == '__main__':
    print(zadanie26(2,3))
    

