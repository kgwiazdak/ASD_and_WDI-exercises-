from math import sqrt
def length(x,y,z):
    odl = sqrt(x**2+y**2+z**2)
    return odl


def exe29(tablica,r, index=0,n=0, x=0,y=0,z=0):

    if n>=3:
        if length(x, y, z) <=r:
            return True
    if index==len(tablica):
        return False

    return zadanie29(tablica,r,index+1, n+1, x+tablica[0],y+tablica[1],z+tablica[2]) | zadanie29(tablica,r,index+1, n,x,y,z)

if __name__ == '__main__':
    from random import randint
    for i in range(10000):
        tablica = [randint(1,20)for _ in range(10)]
        if zadanie29(tablica,10)==True:
            print(True)
            exit()
    print(False)