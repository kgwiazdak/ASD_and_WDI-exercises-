def fibonacci(n):
    arr = [None for _ in range(n)]
    arr[0]=arr[1]=1
    for i in range(2,n):
        arr[i]=arr[i-1]+arr[i-2]

    return arr[n-1]



if __name__ == '__main__':
    print(fibonacci(5))