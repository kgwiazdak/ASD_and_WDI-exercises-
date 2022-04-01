def pole(wspolrzedne):
    x1,x2,y1,y2=wspolrzedne
    a=x2-x1
    b=y2-y1
    return a*b

def czy_nie_nachodza_na_siebie(wspolrzedne1, wspolrzedne2):
    x1, x2, y1, y2 = wspolrzedne1
    a1, a2, b1, b2 = wspolrzedne2
    if (b2<=x1 and a1>=y2) or (a1>=y2 and b1>=x2) or (a1<=y1 and b2<=x1) or (a2<=y1 and b1>=x2):
        return True
    else:
        return False

def zadanie27(T, index=0, tablica=[], surface=0):
    if len(tablica)==13 and surface==2012:
        return True
    if surface>=2012:
        return False
    if index==len(T):
        return False
    bolek = True
    for element in tablica:
        if not czy_nie_nachodza_na_siebie(T[index], tablica[i]):
            bolek=False
            break
    if bolek==True:
        return zadanie27(T, index+1, tablica.append(T[index]), surface+pole(T[index])) | zadanie27(T, index+1, tablica, surface)
    else:
        return zadanie27(T, index+1, tablica, surface)
