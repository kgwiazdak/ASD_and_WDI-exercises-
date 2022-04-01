def heapify(T, n, i):
    l = i * 2 + 1
    p = i * 2 + 2
    m = i
    if l < n and T[m] < T[l]: m = l
    if p < n and T[m] < T[p]: m = p
    if m != i:
        T[m], T[i] = T[i], T[m]
        heapify(T, n, m)


def buildheap(T):
    n = len(T)
    for i in range((n - 1) // 2, -1, -1):
        heapify(T, n, i)


def heapsort(T):
    n = len(T)
    buildheap(T)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)


def parent(i):
    return (i-1)//2


def insert(T, element):
    T.append(element)
    i = len(T)-1
    while T[i]>T[parent(i)]:
        T[i],T[parent(i)]=T[parent(i)], T[i]
        i = parent(i)
    return T




if __name__ == '__main__':
    arr = [3, 23, 6, 23, 6, 24, 2, 46, 233]
    heapsort(arr)
    print(arr)
