

def zadanie17(a, b):
    ile=0
    ca=cb=0
    x,y = a,b
    while x!=0:
        x//=10
        ca+=1
    while y!=0:
        y//=10
        cb+=1

    def prime(number):
        if number == 2 or number == 3:
            return True
        if number % 2 == 0 or number % 3 == 0 or number < 2:
            return False
        from math import sqrt
        for i in range(5, int(sqrt(number)), 2):
            if number % i == 0:
                return False
        return True

    def rek(a,b):
        nonlocal ca,cb,ile
        for index in range(cb+1):
            number = b // (10 ** index) * 10 ** (index + ca) + a * (10 ** index) + b % 10 ** index
            if prime(number):
                ile+=1
    rek(a,b)
    return ile



