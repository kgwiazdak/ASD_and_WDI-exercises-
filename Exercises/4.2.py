def bin_search(T, val):
    left = 0
    right = len(T) - 1
    if right == 0:
        return right if T[right] == val else -1
    while right >= left:
        mid = (left + right) // 2
        if T[mid] == val:
            return mid
        if val > T[mid]:
            left = mid + 1
        else:
            right = mid -1
    return -1


def sort(T):
    values = []

    for i in T:
        if bin_search(values, i) == -1:
            values = [x for x in values if x < i] + [i] + [x for x in values if x > i]


    C = [0] * (len(values))
    B = [0] * (len(T))

    for i in range(len(T)):
        j = bin_search(values, T[i])
        C[j] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range(len(T) - 1, -1, -1):
        j = bin_search(values, T[i])
        C[j] -= 1
        B[C[j]] = T[i]

    for i in range(len(T)):
        T[i]=B[i]

    return T



if __name__ == '__main__':
    arr = [3,3,1,2,1,2,4,4,1,4,3,3,2,1,4,2]
    sort(arr)
    print(arr)