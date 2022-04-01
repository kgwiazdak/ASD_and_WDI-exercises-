def division(number):
    tablica = []
    def rek(number, cur=0, t=[], index=1):
        if number==cur:
            tablica.append(t)
            return True
        if cur>number or (index+cur)>number or index==number-1:
            return False
        tab = t.copy() + [index]
        return rek(number, cur, t, index+1) | rek(number, cur+index, tab, index)
    rek(number)
    return tablica


