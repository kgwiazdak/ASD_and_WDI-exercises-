def czynniki_pierwsze(number):
    tablica = []
    from math import sqrt
    for i in range(3, int(sqrt(number)), 2):
        if number%i==0:
            tablica.append(number)
    if number%2==0:
        tablica.append(2)
    return tablica