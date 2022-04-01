def prime(number):
    if number==2 or number==3:
        return True
    if number%2==0 or number%3==0 or number<2:
        return False
    from math import sqrt
    for i in range(3, int(sqrt(number)), 2):
        if number%i==0:
            return False
    return True