def quicksort(arr):
    n = len(arr)
    p = 0
    r = n - 1
    stos = [[p,r]]
    while len(stos):
        p,r = stos.pop()

        q = partition(arr, p, r)
        if p<q:stos.append((p,q-1))
        if q+1<r:stos.append((q+1, r))


def partition(T, p, r):
    i = p - 1
    x = T[r]
    for j in range(p, r):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1



arr= [3,23,6,43,7,9]
quicksort(arr)
print(arr)