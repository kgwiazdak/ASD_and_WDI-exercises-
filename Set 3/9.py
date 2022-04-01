pamiec = []
def weight(tablica, ile, now=0,n=0,tab=[]):
    global pamiec
    if ile == now:
        pamiec.append(tab)
        return True

    if n==len(tablica):
        return False
    tabmin = tab.copy()
    tabmin.append(-(tablica[n]))
    tabplus = tab.copy()
    tabplus.append(tablica[n])
    return weight(tablica, ile, now, n + 1, tab) | weight(tablica, ile, now + tablica[n], n + 1, tabplus) | weight(
        tablica, ile + tablica[n], now, n + 1, tabmin)



if __name__ == '__main__':
    from random import randint
    tablica = [1, 2, 5, 10, 0.5]
    weight(tablica, 8)
    for element in pamiec:
        print(element)