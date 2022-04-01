def king(T, k):
    l_expensive = 1000000
    def rek(T, w=0, c=0, cost=0):
        nonlocal l_expensive
        if w==8 and cost<l_expensive:
            l_expensive=cost
            return 0
        else:
            return 0

        new_cost = cost + T[w][c]
        if c!=0:
            return rek(T, w+1, c, new_cost) | rek(T, w+1, c-1, new_cost) | rek(T, w+1, c+1, new_cost)
        else:
            return rek(T, w + 1, c, new_cost) | rek(T, w + 1, c + 1, new_cost)

    rek(T,0,k,0)
    return l_expensive


if __name__ == '__main__':
    from random import randint
    tablica = [[randint(1,100)for _ in range(8)]for _ in range(8)]
    print(king(tablica, 3))