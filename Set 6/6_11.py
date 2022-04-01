def enki(T, number):
    licznik = 0
    def rek(T, number, cur=1, index=0):
        nonlocal licznik
        if number==cur:
            licznik+=1
            return True
        if index==len(T) or number<cur or cur==0:
            return False
        return rek(T, number, cur, index+1) | rek(T, number, cur*T[index], index+1)
    rek(T, number)
    return licznik


if __name__ == '__main__':
    print(enki([3,5,64,12,2,1,3,4,8,3,5], 50))