def rek(T, number,cur=0, w=0, k=0):
    if cur==number:
        return True
    if w==8:
        return False
    if k!=7:
        return rek(T, number, cur, w, k+1) | rek(T, number, cur+T[w][k], w+1, 0)
    else:
        cur+=T[w][k]
        return rek(T, number,cur, w+1, 0)

