def LIS(arr):
    n = len(arr)
    F = [1]*n
    P = [-1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[i]>arr[j] and F[i]<F[j]+1:
                F[i]=F[j]+1
                P[i]=j
    return max(F), P

def printing_solution(arr, P, i):
    if P[i]!=-1:
        printing_solution(arr, P, P[i])
    print(arr[i], end=" ")



arr = [13,7,21,42,8,2,44,53]
m, P = LIS(arr)
print(m)
printing_solution(arr, P, len(arr)-1)