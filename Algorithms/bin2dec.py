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