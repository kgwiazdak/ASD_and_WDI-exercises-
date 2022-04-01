def crs(arr, exp):
    n = len(arr)
    C = [0 for _ in range(10)]
    P = [0 for _ in range(n)]

    for i in range(n):
        index = int(arr[i]/exp)
        C[index%10]+=1
    for i in range(1, 10):
        C[i]+=C[i-1]

    for i in range(n-1, -1,-1):
        index = int(arr[i]/exp)
        C[index%10]-=1
        P[C[index%10]]=arr[i]
    for i in range(n):
        arr[i]=P[i]

    return arr


def radix_sort(arr):
    if not arr: return
    max1 = max(arr)
    exp = 1
    while max1/exp>0:
        crs(arr,exp)
        exp*=10

    return arr



if __name__ == '__main__':
    arr = [3, 4, 6, 23, 2, 7, 2, 8, 65, 8, 45, 3, 236, 7, 8, 3, 5, 2, 1, 3, 98, 6, 3, 7]
    radix_sort(arr)
    print(arr)