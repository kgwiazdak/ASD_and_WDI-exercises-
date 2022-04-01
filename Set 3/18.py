def suma(tablica, liczba,w=0, k=0,ile=0, zajete=[-1 for _ in range(8)]):
    if ile ==liczba:
        for element in zajete:
            if element!=-1:
                print(element, end= ' ')
        return True
    if w==8 or w==-1:
        return False

    if k==8:
        b = zajete[w-1]
        ile -= tablica[w-1][b]
        zajete[w-1]=-1
        return suma(tablica,liczba,w-1,b+1,ile,zajete)

    if ile>liczba:
        a = zajete[w-1]
        ile -= tablica[w-1][a]
        zajete[w-1]=-1
        return suma(tablica, liczba,w-1,a+1,ile,zajete)


    if zajete[w]==-1 and (k not in zajete):
        zajete[w]=k
        ile += tablica[w][k]
    else:
        return suma(tablica,liczba,w,k+1,ile,zajete)

    return suma(tablica,liczba,w+1,0,ile,zajete)







if __name__ == '__main__':
    from random import randint
    tablica = [[randint(1,20)for _ in range(8)]for _ in range(8)]
    for element in tablica:
        print(element)
    print()
    for i in range(8):
        suma(tablica,33,0,i)

