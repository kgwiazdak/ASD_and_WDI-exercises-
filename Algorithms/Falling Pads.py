def if_contains(a, b):
    return a[0] <= b[0] and b[1] <= a[1]


def print_solition(i, R):
    if i==-1:
        return
    print_solition(R[i], R)
    print(i, end=" ")
    return


def falling_pads(A):
    n = len(A)

    R = [-1 for _ in range(n)]
    F = [1 for _ in range(n)]
    for i in range(1, n):
        best = 1
        for j in range(i):
            if if_contains(A[j], A[i]):
                q = F[j] + 1
                if best < q:
                    best = q
                    R[i] = j
        F[i] = best
    print_solition(n-1, R)
    print()
    return F[n - 1]


if __name__ == '__main__':
    S = [[-1, 3], [0, 5], [1, 11], [2, 4], [2, 9], [5, 8], [6, 7]]
    print(spadające_kloce(S))
