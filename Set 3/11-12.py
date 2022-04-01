pamiec = []
def exe11(tablica, number, n=0, mult = 1,memory=[]):
    global pamiec
    if number==mult:
        pamiec.append(memory)
        return True

    if n==len(tablica):
        return False

    mem = memory.copy()
    mem.append(tablica[n])
    return exe11(tablica, number, n + 1, mult, memory) | exe11(tablica, number, n + 1, mult * tablica[n], mem)




if __name__ == '__main__':
    from random import randint
    tablica = [3,4,5, 2, 10, 8,13, 11, 7, 3,4,2]
    number = 20
    exe11(tablica, number)
    for element in pamiec:
        print(element)