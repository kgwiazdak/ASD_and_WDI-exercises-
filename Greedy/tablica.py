def string(arr):
    F = [0 for _ in range(26)]
    for i in arr:
        F[ord(i)-97]+=1
    T = []
    T.append(arr[0])
    ile = 0
    for i in range(1, len(arr)):
        if ord(arr[i])>ord(T[len(T)-1]) and arr[i] not in T:
            F[ord(arr[i])-97]-=1
            T.append(arr[i])
        elif ord(arr[i])<ord(T[len(T)-1]) or F[ord(arr[i])-97]==1:
            while T and ord(arr[i])<=ord(T[len(T)-1]) and F[ord(T[len(T)-1])-97]>0:
                T.pop()
            T.append(arr[i])
            F[ord(T[len(T)-1])-97]-=1
    return T


if __name__ == '__main__':
    arr = 'bcabc'
    print(string(arr))