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


def exe1(number, tablica=[], n=1):

    if number//10==0:
        return False

    if number not in tablica:
        if prime(number):
            tablica.append(number)
            print(number)

    if n<=len(str(number)):
        bolec = int(str(number)[0:n-1]+str(number)[n:])
        return exe1(number, tablica, n + 1) or exe1(bolec, tablica, 1)



if __name__ == '__main__':

    number = int(input())
    exe1(number)