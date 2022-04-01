def consistent_substring(T):
    counter = suma = 0
    biggest = 0
    for element in T:
        suma+=element
        if suma<0:
            suma=0
        else:
            biggest=max(biggest, suma)
    return biggest



if __name__ == '__main__':
    T = [2,4,6,-4,-12,8,10,-4]
    print(podciag(T))

