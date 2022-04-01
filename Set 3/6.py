
def exe6(tablica, n=0, suma=0, index = 0):
    if suma==index!=0:
        return suma
    if n == len(tablica):
        return False

    return exe6(tablica, n + 1, suma, index) or exe6(tablica, n + 1, suma + tablica[n], index + n)






if __name__ == '__main__':
    from random import randint
    tablica = [randint(1, 10)for _ in range(10)]
    print(exe6(tablica))

