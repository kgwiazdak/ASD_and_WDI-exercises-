def linear_sieve(n):
    T = [i for i in range(2, n+1)]
    p=2
    i=j=0
    while p*p<=n:
        q=p
        while p*q<=n:
            x=p*q
            while x<=n:
                T.remove(x)
                x=p*x
            i+=1
            q=T[i]
        j+=1
        i=j
        p=T[j]

    return T


if __name__ == '__main__':
    print(sito(50))