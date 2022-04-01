def Fibonacci(n, F):
    if F[n]==None:
        F[n]=Fibonacci(n-1,F)+Fibonacci(n-2,F)
    return F[n]


def funkcja(n):
    F = [None for _ in range(n)]
    F[1]=F[0]=1
    return Fibonacci(n-1, F)


if __name__ == '__main__':
    print(funkcja(5))