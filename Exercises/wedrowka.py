def solution(F, i, j):
    if i==0:
        for k in range(j+1):
            print(arr[0][k], end=" ")
        return 1
    if j==0:
        for k in range(i+1):
            print(arr[k][0], end=" ")
        return 1


    if F[i-1][j]>F[i][j-1]:
        solution(F, i, j-1)
    else:
        solution(F,i-1,j)

    print(arr[i][j], end=" ")




def wedrowka(arr):
    n = len(arr)
    F = [[None]*n for _ in range(n)]
    F[0][0]=0

    s = 0
    for i in range(1, n):
        s+=arr[i][0]
        F[i][0]=s
    s=0
    for i in range(1,n):
        s+=arr[0][i]
        F[0][i]=s

    for i in range(1,n):
        for j in range(1,n):
            F[i][j] = min(F[i-1][j], F[i][j-1])+arr[i][j]

    for el in F:
        print(el)
    print()
    solution(F, n-1, n-1)
    print()

    return F[n-1][n-1]

arr = [[5, 6, 70],
     [1, 22, 1],
     [8, 9, 2]]
print(wedrowka(arr))