def colors(arr):
    kolory = []
    for el in arr:
        if el not in kolory: kolory.append(el)
    ile_kolorow = len(kolory)
    k = []
    c = [0 for _ in range(ile_kolorow)]
    last = 0
    for i in range(len(arr)):
        if arr[i] not in k:
            k.append(arr[i])
        c[kolory.index(arr[i])]+=1
        if arr[i] == arr[last]:
            while c[kolory.index(arr[last])]>1:
                c[kolory.index(arr[last])]-=1
                last+=1
        if len(k)==ile_kolorow:return last,i


arr = ["czerwony", "niebieski","czerwony", "niebieski", "zielony","czerwony"]
print(colors(arr))

