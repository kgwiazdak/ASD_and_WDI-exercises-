def how_many_gasoline(T, i, j,arr,index, czy_podfunkcja):

    if index == len(T[0]):
        return arr

    bolek = False

    arr[index] += T[i][j]
    T[i][j] = 0


    if j<len(T[0])-1 and T[i+1][j]!=0:  #dół
        how_many_gasoline(T, i, j + 1, arr, index, True)
        bolek=True


    if i<len(T)-1 and T[i+1][j]!=0: #prawo
        how_many_gasoline(T, i + 1, j, arr, index, True)
        bolek = True

    if i > 0 and T[i-1][j]!=0:  #w górę
        how_many_gasoline(T, i - 1, j, arr, index, True)
        bolek = True

    if j>0 and T[i][j-1]!=0:    #lewo
        how_many_gasoline(T, i, j - 1, arr, index, True)
        bolek = True



    if not bolek and not czy_podfunkcja:
        return how_many_gasoline(T, 0, index + 1, arr, index + 1, False)

    return 




if __name__ == '__main__':
    T = [
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    arr = [0 for _ in range(len(T[0]))]
    q = how_many_gasoline(T, 0, 0, arr, 0, False)
    for i in arr:
        print(i, end=" ")

    print()

