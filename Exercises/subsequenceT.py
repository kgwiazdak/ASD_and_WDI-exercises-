def sumadoT(arr, value):
    n = len(arr)
    subsequence = [[False]*(value+1)for _ in range(n+1)]
    for i in range(n+1):subsequence[i][0]=True
    for i in range(1, value+1):subsequence[0][i]=False

    for i in range(1,n+1):
        for j in range(1,value+1):
            subsequence[i][j]=subsequence[i-1][j]
            if j>=arr[i-1]:
                subsequence[i][j] = subsequence[i][j] or subsequence[i-1][j-arr[i-1]]
    for el in subsequence:
        print(el)
    return subsequence[n][value]


A = [ 4, 234 ,5 ,6346 ,45 ,745 ,7 ,45 ,7, 0, 2]
suma = sum(A)
suma-=6346
suma-=745
suma-=234

print(sumadoT(A, suma))