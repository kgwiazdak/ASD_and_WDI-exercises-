from cmath import inf

def solution(arr, F, value):
    if value<=0:return
    for el in arr:
        if F[value-el]+1==F[value]:
            solution(arr, F, value-el)
            print(el, end = " ")
            break

def rek(arr, F, value):
    if value<0: return inf
    if F[value]!=inf:
        return F[value]
    v_min = inf
    for el in arr:
        v_min = min(v_min, rek(arr, F, value-el)+1)
    F[value]=v_min
    return F[value]

def monety(arr, value):
    n = value+1
    F = [inf for _ in range(n)]
    F[0]=0
    return rek(arr, F, value), F


arr = [1,5,8]
ile, F = monety(arr, 15)
solution(arr, F,15)
print()
print(ile)