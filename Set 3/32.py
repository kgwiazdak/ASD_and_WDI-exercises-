def suma(zbior1, zbior2):
    add = 0
    for i in zbior1:
        add+= i
    for i in zbior2:
        add+=i
    return add


def exe32(tablca, number, index =0, zbior1=[], zbior2=[]):
    if len(zbior1)==len(zbior2) and suma(zbior1,zbior2)==number:
        return True
    if index==len(tablca):
        return False
    nowy1=zbior1
    nowy1.append(index)
    nowy2 = zbior2
    nowy2.append(index)

    return exe32(tablca, number, index + 1, zbior1, zbior2) | exe32(tablca, number, index + 1, nowy1, zbior2) | exe32(
        tablca, number, index + 1, zbior1, nowy2)

if __name__ == '__main__':
    from random import randint
    tablica = [randint(1,20)for _ in range(20)]
    print(exe32(tablica, 30))