def obszar(arr, k):
    ile = 0
    pointer = k-1
    while arr[pointer]!=1:
        pointer-=1
    if pointer==0:return -1
    else:ile+=1

    while pointer+k<len(arr):
        curr = pointer+k
        while arr[curr]!=1:curr-=1
        if curr==pointer:return -1
        else:
            pointer=curr
            ile+=1
    return ile


if __name__ == '__main__':
    arr = [0,0,1,0,1,1,0,0,1,0,1,1,1,1]
    print(obszar(arr, 4))