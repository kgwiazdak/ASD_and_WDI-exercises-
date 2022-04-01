def sys_change(number, base):
    T = []
    while number!=0:
        sth = number%base
        T.append(sth)
        number//=base
    n = len(T)
    finish = 0
    for i in range(1,n+1):
        finish=(finish+T[n-i])*10
    return finish//10



