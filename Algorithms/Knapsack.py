def knapsack(P,W, MaxW):
    n = len(P)
    F = [[0] * (MaxW + 1)for _ in range(n)]

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]


    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])
    for el in F:
        print(el)
    print(solution(P,W,MaxW,F,n-1))
    return F[n-1][MaxW]


def solution(P, W, MaxW, F, i):
    if i<0: return []
    if i==0:
        if W[i]>MaxW: return []
        else: return [0]
    if MaxW>=W[i] and F[i][MaxW]==F[i - 1][MaxW - W[i]] + P[i]: return solution(P,W,MaxW-W[i],F, i-1)+[i]
    return solution(P,W,MaxW,F,i-1)



P  = [10,8,4,5,3,7]
W = [4,5,12,9,1,13]
print(knapsack(P,W,24))





