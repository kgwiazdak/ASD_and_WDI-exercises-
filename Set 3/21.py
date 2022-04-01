tablica = []
def exe21(A,B):
    liczba = 1
    A-=1
    def rek(A,B,liczba):
        global tablica
        if A==B==0:
            tablica.append(liczba)
            return True
        if A!=0 and B!=0:
            return rek(A-1, B, liczba*10+1) | rek(A,B-1,liczba*10)
        if A==0:
            return rek(A,B-1,liczba*10)
        if B==0:
            return rek(A-1, B, liczba*10+1)
    rek(A,B,liczba)
    return tablica



if __name__ == '__main__':
    print(zadanie21(3,4))