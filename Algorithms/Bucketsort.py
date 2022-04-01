def insert_sort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j > 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j] = key
    return T


def bucket_sort(A):
    n = len(A)
    B = []
    for _ in range(n):
        B.append([])

    for i in A:
        id = int(n * i)
        B[id].append(i)

    for i in range(n):
        B[i] = insert_sort(B[i])

    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1
    return A



if __name__ == '__main__':
    T = [0.4342,0.654,0.12,0.876,0.123,0.234,0.0987,0.5674,0.978]
    print("Sorted Array is")
    print(bucket_sort(T))