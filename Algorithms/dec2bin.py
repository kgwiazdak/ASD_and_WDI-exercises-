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