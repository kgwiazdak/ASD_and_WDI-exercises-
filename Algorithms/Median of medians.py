def median_of_medians(arr,k):
    if arr is None or len(arr) == 0:
        return None
    return select_pivot(arr, k)


def select_pivot(arr, k):
    chunks = [arr[i: i + 5] for i in range(0, len(arr), 5)]
    sorted_chunks = [sorted(chunk) for chunk in chunks]
    medians = [chunk[len(chunk) // 2] for chunk in sorted_chunks]

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = select_pivot(medians, len(medians) // 2)

    p = partition(arr, pivot)

    if k == p:
        return pivot
    if k < p:
        return select_pivot(arr[0:p], k)
    else:
        return select_pivot(arr[p + 1:len(arr)], k - p - 1)


def partition(arr, pivot):
    left = 0
    right = len(arr) - 1
    i = 0

    while i <= right:
        if arr[i] == pivot:
            i += 1

        elif arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
    return left


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 1000, 8, 9, 99]
    print(median_of_medians(arr, 0))
