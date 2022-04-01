def countsort(T, k):
    k+=1
    B = [0 for _ in range(len(T))]
    C = [0 for _ in range(k)]

    for i in range(len(T)):
        C[T[i]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(len(T) - 1, -1, -1):
        C[T[i]]-=1
        B[C[T[i]]]=T[i]

    for i in range(len(T)):
        T[i] = B[i]

    return T

arr = [3,2,63,23,62,6345,23,6]
print(countsort(arr,6345))


