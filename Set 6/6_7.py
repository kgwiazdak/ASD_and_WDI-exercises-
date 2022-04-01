def waga(number):
    odwazniki = [1,2,5,9]
    def rek(odwazniki, number, cur=0, index = 0):
        if cur==number:
            return True
        if index==len(odwazniki):
            return False
        return rek(odwazniki, number, cur, index+1) | rek(odwazniki, number, cur+odwazniki[index], index+1)
    return rek(odwazniki, number)



