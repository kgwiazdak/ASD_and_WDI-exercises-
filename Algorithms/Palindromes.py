def palindromy(string):
    n = len(string)
    arr=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        arr[i][i]=1
    for c in range(2,n+1):
        for i in range(n-c+1):
            j = c+i-1
            if string[i]==string[j] and c==2:
                arr[i][j]=2
            elif string[i]==string[j]:
                arr[i][j]=arr[i+1][j-1]+2
            else:
                arr[i][j]==max(arr[i+1][j], arr[i][j-1])
    return arr[0][n-1]


if __name__ == '__main__':
    print(palindromy("babcbab"))