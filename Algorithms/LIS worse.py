def print_lcs(X, b, i, j):
    if i == 0:
        return
    if b[i][j] == 2:
        print_lcs(X, b, i - 1, j - 1)
        print(X[i-1], end=" ")
    elif b[i][j] == 1:
        print_lcs(X, b, i - 1, j)
    else:
        print_lcs(X, b, i, j - 1)
    return


def print_solution(X, c, i, j):
    if i == 0:
        return
    if c[i][j] == c[i - 1][j - 1] + 1:
        print_solution(X, c, i - 1, j - 1)
        print(X[i-1], end=" ")
    elif c[j-1][i] <= c[i - 1][j]:
        print_solution(X, c, i - 1, j)
    else:
        print_solution(X, c, i, j - 1)
    return


def lcs(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 2
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 1
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 0
    return c, b


if __name__ == '__main__':
    X = [1, 0, 0, 1, 0, 1, 0, 1]
    Y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

    m = len(X)
    n = len(Y)

    c, b = lcs(X, Y)

    print(c[m][n])
    print_lcs(X, b, m, n)
    print()
    print_solution(X, c, m, n)


