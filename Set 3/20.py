koncowo = []
finish = []

def exe23(tablica, indeks=0, x1=0,y1=0,n1=0, x2=0,y2=0,n2=0):
    global koncowo
    global finish
    if indeks==len(tablica):
        return True
    if n1!=0 and (x1/n1, y1/n1) not in koncowo:
        koncowo.append((x1/n1, y1/n1))
    if n2!=0 and (x2/n2, y2/n2) not in finish:
        finish.append((x2/n2, y2/n2))
    return exe23(tablica, indeks + 1, x1 + tablica[indeks][0], y1 + tablica[indeks][1], n1 + 1, x2, y2, n2) | exe23(
        tablica, indeks + 1, x1, y1, x2 + tablica[indeks][0], y2 + tablica[indeks][1], n2 + 1)


if __name__ == '__main__':
    import random
    tablica= [(random.random()*random.randint(-100, 100), random.random()*random.randint(-100, 100)) for _ in range(10)]
    print(exe23(tablica))
    koncowo.sort()
    finish.sort()
    print(finish[0])
    print(koncowo[0])