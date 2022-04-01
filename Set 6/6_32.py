def rek(T, number, index=0, A=0, B=0):
    if A==B==number:
        return True
    if index==len(T):
        return False
    if A>=number or B>=number:
        return False
    return rek(T, number, index+1, A, B) | rek(T, number, index+1, A+T[index], B) | rek(T, number, index+1, A,B+T[index])


