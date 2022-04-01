def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q - p < r - q:
            quicksort(T, p, q - 1)
            p = q + 1
        else:
            quicksort(T, q + 1, r)
            r = q-1


def partition(T, p, r):
    i = p - 1
    x = T[r]
    for j in range(p, r):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1



if __name__ == '__main__':
    T = [2, 4, 6, -4, -12, 8, 10, -4]
    quicksort(T,0, len(T)-1)
    print(T)
