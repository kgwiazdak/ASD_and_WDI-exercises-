def how_many_ones(number):
    suma = 0
    while number>0:
        if number%2==0:
            number//=2
        else:
            suma+=1
            number-=1
            number//=2

    return suma


def exe28(tablica, nowa=[]):
    for element in tablica:
        nowa.append(how_many_ones(element))
    def rek(nowa, index = 0, zbior1=0, zbior2=0, zbior3=0):
        if index==len(nowa):
            if zbior1==zbior2==zbior3: return True
            else: return False
        return rek(nowa, index+1, zbior1+nowa[index],zbior2,zbior3) | rek(nowa, index+1, zbior1,zbior2+nowa[index],zbior3) | rek(nowa, index+1, zbior1,zbior2,zbior3+nowa[index])

    return rek(nowa)



if __name__ == '__main__':
    from random import randint
    tablica = [randint(1, 20)for _ in range(10)]
    print(zadanie28(tablica))


