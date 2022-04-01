from cmath import inf

def solution(P, W, H, F, i,j,k):
    if i<0:return []
    if j>=W[i] and k>=H[i]:
        if F[i][j][k]==F[i-1][j-W[i]][k-H[i]]+P[i]:
            return solution(P, W, H, F, i-1,j-W[i],k-H[i])+[i]
    return solution(P, W, H, F, i-1,j,k)

def rek(P, W, H, MaxW, MaxH, F, i, j, k):
    if i<0:return -inf
    if F[i][j][k]!=-inf:return F[i][j][k]
    F[i][j][k]=rek(P, W, H, MaxW, MaxH, F, i-1, j, k)
    if j>=W[i] and k>=H[i]:
        F[i][j][k] = max(rek(P, W, H, MaxW, MaxH, F, i-1, j-W[i], k-H[i])+P[i], F[i][j][k])
    return F[i][j][k]

def knapsack2D(P, W, H, MaxW, MaxH):
    n = len(P)

    F = [[[-inf for _ in range(MaxH+1)]for _ in range(MaxW+1)]for _ in range(n)]

    for i in range(n): F[i][0][0] = 0

    for w in range(MaxW + 1):
        for h in range(MaxH + 1):
            if w >= W[0] and h >= H[0]:
                F[0][w][h] = P[0]
            else:
                F[0][w][h] = 0


    best = rek(P, W, H, MaxW, MaxH, F, n-1, MaxW, MaxH)
    print(solution(P,W,H,F, n-1, MaxW, MaxH))
    return best

P = [5,12,7,1,56,4]
W = [1,11,9,4,10,2]
H = [7,13,1,9,27,1]

print(knapsack2D(P, W, H, 20, 35))



