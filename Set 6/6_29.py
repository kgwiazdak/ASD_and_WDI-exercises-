def zadanie29(T, r):
    def rek(T, r,index=0, tablica=[]):
        if index==len(T):
            return False
        x=y=z=0
        for element in tablica:
            x+=element[0]
            y+=element[1]
            z+=element[2]
        from math import sqrt
        odleglosc =sqrt(x**2+y**2+z**2)
        if len(tablica)>=3 and odleglosc<=r:
            return True
        return rek(T, r, index+1, tablica.append(T[index])) | rek(T, r, index+1, tablica)