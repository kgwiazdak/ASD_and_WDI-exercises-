from cmath import inf


def memorized_cut_road(P):
    n = len(P)
    r = [-inf for _ in range(n)]
    return cut_road(P, r, n-1)


def cut_road(P, r, n):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -inf
        for i in range(n):
            q = max(q, P[i]+cut_road(P, r, i))
    r[n] = q
    print(r)
    return r[n]


if __name__ == '__main__':
    P = [0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
    print(memorized_cut_road(P))
