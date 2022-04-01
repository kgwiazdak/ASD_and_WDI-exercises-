from math import ceil, sqrt

def prime(n):
    if n==2 or n==3 or n==5 or n==7: return True
    if n%2==0: return False
    for i in range(3, ceil(sqrt(n)), 2):
        if n%i==0:return False
    return True

def zadanie(number):
    i = 1
    solution = [-1, -1]
    best = float("inf")
    while True:
        n1 = number // 10 ** i
        n2 = number % 10 ** i
        if n1==0:break
        if prime(n1) and prime(n2):
            eq = n1 * n2
            if eq < best:
                best = eq
                solution[0] = n1
                solution[1] = n2
        i+=1
    return solution


if __name__ == '__main__':
    print(zadanie(1372))