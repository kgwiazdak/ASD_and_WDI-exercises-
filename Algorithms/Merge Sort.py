def merge_sort(T):
    while True:
        inversion = []
        for i in range(len(T) - 1):
            if T[i] > T[i + 1]:
                inversion.append(i)
        inversion.append(len(T) - 1)

        if len(inversion) == 1:
            return T

        p = 0
        while len(inversion) > 1:
            merge(T, p, inversion[0], inversion[1])
            p = inversion[1] + 1
            inversion = inversion[2:]


def merge(T, p, q, r):
    A = T[p:q+1]
    B = T[q + 1:r+1]
    i = p

    while len(A) != 0 and len(B) != 0:
        if A[0] >= B[0]:
            T[i] = B.pop(0)
            i += 1
        else:
            T[i] = A.pop(0)
            i += 1
    while len(A) > 0:
        T[i] = A.pop(0)
        i += 1
    while len(B) > 0:
        T[i] = B.pop(0)
        i += 1
    return T


if __name__ == '__main__':
    T = [2, 4, 6, -4, -12, 8, 10, -4]
    print(merge_sort(T))
