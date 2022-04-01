def zadanie6(T):
    najmniejszy = 9999999999
    def rek(T, s_elementow=0, s_indexow=0, index=0):
        nonlocal najmniejszy
        if s_indexow == s_elementow!=0:
            if s_indexow<najmniejszy:
                najmniejszy=s_indexow
            return True
        if index == len(T):
            return False
        return rek(T, s_elementow + T[index], s_indexow+index, index + 1) | rek(T, s_elementow, s_indexow,index + 1)
    rek(T)
    return najmniejszy if najmniejszy!=9999999999 else 0



if __name__ == '__main__':
    print(zadanie6( [ 1,7,3,5,11,2 ] ))