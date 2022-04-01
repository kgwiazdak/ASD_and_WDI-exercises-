from cmath import inf
def contains(arr, middle):
    for i in range(len(arr)):
        if middle>arr[i][3] and middle<arr[i][1]: return False
    return True

def odjac(arr, middle, V):
    M = V
    ile = 0
    for i in range(len(arr)):
        if arr[i][1]<=middle:
            surface = (arr[i][2]-arr[i][0])*(arr[i][1]-arr[i][3])
            V-=surface
            ile+=1
            if V<0: return -1, -1
    if M!=V:return V, ile
    else: return -2,-1


def zbiorniki(arr, V):
    min1 = inf
    max1 = -inf
    ile = 0
    x=1
    for i in range(len(arr)):
        min1 = min(min1,arr[i][3])
        max1 = max(max1, arr[i][1])
    middle = (min1+max1)//2
    while x>0 and min1<max1:

        x, ile = odjac(arr, middle, V)
        if x==-1: max1=middle-1
        elif x==-2: min1=middle+1
        else: min1 = middle

        middle = (min1 + max1) // 2
        if x==-1: x=1
        if x==-2: x=1
    x, ile = odjac(arr, middle, V)
    return ile


arr = [(3,4,5,1),(6,5,8,3), (3,10, 6,7)]
print(zbiorniki(arr, 7))