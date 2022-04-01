from cmath import inf


dp = [[-1 for _ in range(100)]for _ in range(100)]

def matrix(p, i, j):

    if i==j:
        return 0

    if (dp[i][j] != -1):
        return dp[i][j]

    dp[i][j]=inf

    for k in range(i,j):
        dp[i][j] = min(dp[i][j], matrix(p, i, k) + matrix(p, k+1, j) + p[i-1]*p[k]*p[j])

    return dp[i][j]


arr = [2,3,4,5,6]
print(matrix(arr, 1, len(arr)-1))