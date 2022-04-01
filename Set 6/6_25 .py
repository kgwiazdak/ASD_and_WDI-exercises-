def skok(T):
    def pierwsze(number):
        tablica = []
        from math import sqrt
        for i in range(3, int(sqrt(number))+1, 2):
            if number % i == 0:
                tablica.append(i)
        if number % 2 == 0:
            tablica.append(2)
        return tablica

    def rek(T, index=0, czynniki=[], i=0, counter=0):
        czynniki=pierwsze(T[index])
        if index==len(T)-1:
            return counter
        if i==len(czynniki)!=0:
            return False
        if index+czynniki[i] >= len(T):
            return rek(T, index, pierwsze(T[index]), i+1, counter)
        else:
            new_index = index+czynniki[i]
            return rek(T, index, pierwsze(T[index]), i+1, counter) | rek(T, new_index, pierwsze(T[index]), 0, counter+1)

    return rek(T)


if __name__ == '__main__':
    tablica = [15, 6, 8, 32]
    print(skok(tablica))