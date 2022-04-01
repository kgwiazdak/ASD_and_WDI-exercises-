def weight(tablica, ile, now=0,n=0):
    if ile == now:
        return True
    if n==len(tablica):
        return False
    return weight(tablica, ile, now, n + 1) | weight(tablica, ile, now + tablica[n], n + 1) | weight(tablica,
                                                                                                     ile + tablica[n],
                                                                                                     now, n + 1)




if __name__ == '__main__':
    from random import randint
    tablica = [randint(1,10)for _ in range(10)]
    print(weight(tablica, 2))