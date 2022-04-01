def exe4(tablica, n=1, wiersz =0, kolumna = 0, memory = []):
    memory.append((wiersz,kolumna))
    if n==len(tablica)**2+1:
        for element in tablica:
            if 0 in element:
                return False
        return memory

    moves = [exe4(tablica, n + 1, wiersz + 2, kolumna - 1, memory),
             exe4(tablica, n + 1, wiersz + 2, kolumna + 1, memory), exe4(tablica, n + 1, wiersz + 1, kolumna + 2,
                                                                         memory), exe4(tablica, n + 1, wiersz - 1,
                                                                                       kolumna + 2, memory), exe4(
            tablica, n + 1, wiersz - 2, kolumna + 1, memory), exe4(tablica, n + 1, wiersz - 2, kolumna - 1, memory), exe4(
            tablica, n + 1, wiersz - 1, kolumna - 2, memory), exe4(tablica, n + 1, wiersz + 1, kolumna - 2, memory)]

    

if __name__ == '__main__':
    n = 8
    tablica = [[0 for _ in range(n)]for _ in range(n)]
    print(exe4(tablica))