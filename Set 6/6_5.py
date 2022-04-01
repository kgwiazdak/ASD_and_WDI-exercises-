def if_prime(number):
    if number%2==0 or number%3==0:
        return False
    from math import sqrt
    for i in range(3, int(sqrt(number)), 2):
        if number%i==0:
            return False
    return True
def zadanie5(T):
    number = 0
    for element in T:
        number*10
        number+=element

        def zera(T, number, index=1):
            if if_prime(number):
                return True
            if number//index==0:
                return False
            else:   return (zera(T, number//(10**index), 1) and zera(T, number%(10**(index+1)), 1)) | zera(T, number, index+1)
    return zera(T,number)






