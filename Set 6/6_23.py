def oporniki(T, number, cur=0,rownolegle=0, liczba=0, index=0):
    if cur==number:
        return True
    if liczba!=0:
        if rownolegle/liczba==number:
            return True

    if cur>number or index==len(T):
        return False
    return oporniki(T, number, cur+T[index], rownolegle, liczba, index+1) or oporniki(T, number, cur, rownolegle, liczba, index+1) or oporniki(T, number, cur, rownolegle+T[index], liczba+1, index+1)

