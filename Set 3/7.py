def weight(arr, ile, now=0, n=0):
    if ile == now:
        return True
    if n==len(arr):
        return False
    return weight(arr, ile, now + arr[n], n + 1) | weight(arr, ile, now, n + 1)
if __name__ == '__main__':
    from random import randint
    tablica = [1, 2, 3, 4, 5, 6, 7]
    print(weight(tablica, 16))
