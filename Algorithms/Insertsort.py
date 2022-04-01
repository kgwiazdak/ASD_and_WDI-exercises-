def insert_sort(T):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        j = i - 1
        while j > 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j] = key
    return T