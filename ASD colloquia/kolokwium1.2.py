def bin_to_dec(W):
    n=len(W)
    number = 0
    for i in range(n):
        number+=(2**(n-1-i))*W[i]
    return number

def odl_pom_bin(T):
    n=len(T[0])
    biggest=(0,0)
    second=(-1,0)
    for i in T:
        number = bin_to_dec(i)
        if number>biggest[0]:
            second=biggest
            biggest=(number,T.index(i))
        elif number<biggest[0] and number>second[0]:
            second=(number,T.index(i))
    return abs(biggest[1]-second[1])



if __name__ == '__main__':
    from random import randint
    n=1000
    T=[[randint(0,1)for _ in range(n)]for _ in range(n)]

    print(odl_pom_bin(T))