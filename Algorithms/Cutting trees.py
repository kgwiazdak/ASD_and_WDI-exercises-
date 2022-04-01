def print_solution(i, F, A):
    if i<2:
        if A[1]>A[0] and A[1]>0: print(1)
        elif A[0]>A[1] and A[0]>0: print(0)
        return

    if F[i]==F[i-2]+A[i]:
        print_solution(i-2, F, A)
        print(i)
    else: print_solution(i-1, F, A)


def las(A):
    n = len(A)
    F=[0 for _ in range(n)]
    F[0]=max(0, A[0])
    F[1]=max(0, A[0], A[1])

    for i in range(2, n):
        F[i]=max(F[i-2]+A[i], F[i-1])

    print_solution(n-1, F, A)



if __name__ == '__main__':
    C = [2, 4, 5, 100, 15, 4, 12]
    las(C)