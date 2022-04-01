def suma(T,w,k):
    add = 0
    for i in range(len(T)):
        add += T[w][i] + T[i][k]
    add -= 2*T[w][k]
    return add          #suma szachowanych pol



def chess(T):
    najwieksza = 0
    wsp = (0,0,0,0)
    tablica = [0 for _ in range(len(T))]
    for wiersz in range(len(T)-1):
        for kolumna in range(len(T)):
            for w in range(1,len(T)):
                if w == wiersz:
                    continue
                for k in range(len(T)):
                    if k == kolumna:
                        continue
                    if suma(T,w,k)+suma(T,wiersz,kolumna)>najwieksza:
                        najwieksza= suma(T,w,k)+suma(T,wiersz,kolumna)
                        wsp = (wiersz, kolumna, w,k)
    return wsp



if __name__ == '__main__':
    from random import randint
    n=30
    tablica = [[randint(1,30)for _ in range(n)]for _ in range(n)]
    print(chess(tablica))