
def zadanie(arr, ile):
    gasoline = ile
    for i in range(len(arr)-1):
        gasoline-=arr[i]

        if gasoline+arr[i]-arr[i+1]<0: gasoline=ile
        if gasoline+arr[i]-arr[i+1]<0: return False

    if gasoline+arr[len(arr)-2]-arr[len(arr)-1]<0:return False
    return True

if __name__ == '__main__':
    arr = [0,2,3,5,8,11,13,17]
    print(zadanie(arr, 5))