def solution(F, arr, A, i, g, d):
    if i>0:
        if g+arr[i-1]<=A:
            if F[i-1][g+arr[i-1]][d]:
                solution(F, arr, A, i-1, g+arr[i-1], d)
                print(f"G: {arr[i-1]}")
        if d+arr[i-1]<=A:
            if F[i-1][g][d+arr[i-1]]:
                solution(F, arr, A, i-1, g, d+arr[i-1])
                print(f"D: {arr[i-1]}")


def rek(arr, F, A, i, g, d):
    if i<0:return False
    if F[i][g][d] is not None:return F[i][g][d]

    q = False
    if g+arr[i-1]<=A:
        q = q or rek(arr, F, A, i-1, g+arr[i-1], d)
    if not q and d+arr[i-1]<=A:
        q = rek(arr, F, A, i-1, g, d+arr[i-1])
    F[i][g][d]=q
    return F[i][g][d]

def prom(arr, A):
    n = len(arr)
    F = [[[None for _ in range(A+1)]for _ in range(A+1)]for _ in range(n+1)]

    for i in range(A+1):
        for j in range(A+1):
            F[0][i][j]=True

    for i in range(n, -1, -1):
        for g in range(A+1):
            for d in range(A+1):
                if rek(arr, F, A, i, g, d):
                    solution(F, arr, A, i, g, d)
                    return i, g, d

A = [ 1, 2, 3, 3, 7 ]
print(prom(A, 5))