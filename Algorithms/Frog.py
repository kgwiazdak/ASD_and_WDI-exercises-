from cmath import inf
def solution(arr, F, i, j):
    if i<1:return []

    for k in range(1, i+1):
        if j+k-arr[i]<=0:continue
        if F[i-k][j+k-arr[i]]+1==F[i][j]:
            return solution(arr, F, i-k, j+k-arr[i])+[i]

def print_solution( i, j, A, F ):
    if i > 0:
        for k in range(1, i+1):
            if j+k-A[i] <= 0: continue
            if F[i][j] == F[i-k][j+k-A[i]]+1:
                print_solution( i-k, j+k-A[i], A, F )
                break
    print(i, end=' ')




def rek(arr,F, i, j):
    if i<0:return inf
    if j<=0 or j>sum(arr):return inf
    if F[i][j]!=inf:return F[i][j]

    best = inf
    for k in range(1, i+1):
        if j+k-arr[i]<k:break
        best=min(best, rek(arr, F, i-k, j+k-arr[i])+1)
    F[i][j]=best
    return F[i][j]

def zaba(arr):
    n = len(arr)
    suma = sum(arr)

    F = [[inf for _ in range(suma+1)]for _ in range(n)]
    F[0][arr[0]]=0

    best = inf
    index = -1
    for i in range(suma+1):
        if best > rek(arr, F, n-1, i):
            index=i
            best=rek(arr, F, n-1, i)

    for el in F:print(el)
    print(solution(arr, F, n-1, index))
    print()
    return best

A = [ 2, 1, 1, 1, 4, 2, 3, 1, 1, 1, 1, 1, 1 ]
print(zaba(A))