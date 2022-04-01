def if_prime(number):
    if number<10 or number%2==0 or number%3==0:
        return False
    from math import sqrt
    for i in range(3, int(sqrt(number)), 2):
        if number%i==0:
            return False
    return True


def cut(number):
    ile = number
    n=0
    while ile!=0:
        ile//=10
        n+=1
        iles = number
    def rek(number, index=n-1, len=n, counter=0):
        if index==-1:
            return counter
        if if_prime(number) and number!=iles:
            counter+=1
        if len==index+1:
            return rek(number, index-1, n, counter)
        else:
            n_num = number//(10**(len-index))+number%10**(len-index)
            return rek(number, index-1, n, counter) | rek(n_num, index-1, n-1, counter)
    return rek(number, n-1, n, 0)


