def spr(arr, val):
    start =0
    suma = 0
    for i in range(len(arr)):
        if arr[i]+suma==val:return start,i
        elif arr[i]+suma<val:suma+=arr[i]
        elif arr[i]>val:
            suma=0
            start=i+1
        else:
            while suma+arr[i]>val:
                suma-=arr[start]
                start+=1
            suma+=arr[i]
            if arr[i] + suma == val: return start, i
    return -1

arr = [14,7,3,91,4,5,8,3,2]
print(spr(arr,20))

