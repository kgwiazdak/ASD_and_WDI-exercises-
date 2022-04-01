def fueling(T, d, F):
    n = len(T)
    if F-T[n-1]>d:
        return None
    x = 0
    stacja = 0
    i=0
    while i<n-1:
        if T[i+1]-x>=d:
            stacja+=1
            if T[i+1]-x>d:
                x=T[i]
                i-=1
            else: x=T[i+1]
        i+=1
    if F-x>d: stacja+=1
    return stacja


if __name__ == '__main__':
    arr= [0,2,3,5,8,11,13,17]
    print(tankowanie(arr, 5, 21))