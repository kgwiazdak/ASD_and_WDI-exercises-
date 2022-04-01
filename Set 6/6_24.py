def zadanie24(T):
    from math import sqrt
    odleglosc = 99999999999999999
    def punkty(T, x1=0, y1=0, l1=0, x2=0,y2=0, l2=0, index=0):
        if index==len(T):
            return False


        if l1 != 0 and l2 != 0:
            dx1=x1/l1
            dy1=y1/l1
            dx2=x2/l2
            dy2=y2/l2
            nonlocal odleglosc
            distance = sqrt((dx2-dx1)**2+(dy2-dy1)**2)
            if distance<odleglosc:
                odleglosc=distance

        if l1==0 and l2==0 and index==len(T)-2:
            return punkty(T, x1+T[index][0], y1+T[index][1],l1+1, x2, y2, l2,index+1) | punkty(T, x1, y1, l1, x2+T[index][0], y2+T[index][1], l2+1, index+1)
        if l1==0 and index==len(T)-1:
            return punkty(T, x1+T[index][0], y1+T[index][1],l1+1, x2, y2, l2,index+1)
        if l2==0 and index==len(T)-1:
            return punkty(T, x1, y1, l1, x2+T[index][0], y2+T[index][1], l2+1, index+1)
        return punkty(T, x1, y1, l1, x2,y2, l2, index+1) | punkty(T, x1+T[index][0], y1+T[index][1],l1+1, x2, y2, l2,index+1) | punkty(T, x1, y1, l1, x2+T[index][0], y2+T[index][1], l2+1, index+1)
    punkty(T)
    return odleglosc

