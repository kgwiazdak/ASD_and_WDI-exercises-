def partition(arr, p,r):
    i = p-1
    x = arr[r]
    for j in range(p,r):
        if arr[j]<=x:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


def kthSmallest(arr, p,r,k):
    if (k>=0 and k<=r-p+1):
        index = partition(arr, p, r)
        if index-p==k:
            return arr[index]
        if index-p>k:
            return kthSmallest(arr,p,index-1,k)
        return kthSmallest(arr, index+1, r, k-index+p)


arr = [2,6,4,8,5]
print(kthSmallest(arr,0,len(arr)-1,0))