def way_home(T):
    n = len(T)
    arr = [1 for _ in range(n)]
    for i in range(n-3, -1,-1):
        suma=0
        for j in range(i+1, i+ T[i]+1):
            if j==n:break
            suma+=arr[j]
        arr[i]=suma

    return arr[0]



if __name__ == '__main__':
    arr = [2,1,3,2,1,0]
    print(wariat(arr))

