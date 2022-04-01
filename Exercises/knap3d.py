def knapsack(W, D1, D2, MaxD1, MaxD2):
    n = len(W)
    arr = [[[[0]*(MaxD1+1)]for _ in range(MaxD2+1)]for _ in range(n)]

    for i in range(n):
        for j in range(MaxD1+1):
            arr[0][i][j]=0

    for i in range(n):
        for j in range(MaxD1 + 1):
            arr[j][i][0] = 0

    for i in range(n):
        for j in range(MaxD1+1):
            arr[i][0][j]=0


    for i in range(1,n):
        for j in range(1, MaxD1+1):
            for k in range(1, MaxD2+1):
                if D1[i-1]>j or D2[i-1]>k:
                    arr[i][j][k]=arr[i-1][j][k]
                else:
                    arr[i][j][k]=max(arr[i-1][j][k],arr[i-1][j-D1[i-1]][k-D2[i-1]]+W[i-1])

    return arr[n-1][MaxD1][MaxD2]
