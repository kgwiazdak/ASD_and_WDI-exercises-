def suma(T,w,k):
    add = 0
    for i in range(len(T)):
        add += T[w][i] + T[i][k]
    add -= 2*T[w][k]
    return add




def chess1(T):
    najwieksza1 = 0
    najwieksza2=0
    wsp = (0,0,0,0)
    wsp1=[0 for i in range(2)]
    wsp2=[0 for i in range(2)]
    for wiersz in range(len(T)):
        for kolumna in range(len(T)):
                    if najwieksza1<suma(T, wiersz,kolumna):
                        najwieksza1=suma(T,wiersz,kolumna)
                        wsp1[0] = wiersz
                        wsp1[1] = kolumna
                    elif najwieksza2<suma(T, wiersz,kolumna):
                        najwieksza2=suma(T,wiersz,kolumna)
                        wsp2[0] = wiersz
                        wsp2[1] = kolumna
    wsp = (wsp1[0],wsp1[1],wsp2[0],wsp2[1])
    return wsp