def value(T, val):
    left = 0
    right = len(T)-1
    if right==0:
        return right if T[right]==val else False
    while right>=left:
        mid = (left+right)//2
        if T[mid]==val:
            return mid
        if val > T[mid]:
            left=mid+1
        else:
            right=mid
    return False


if __name__ == '__main__':
    T = [3,6,8,35,2564]
    print(value(T, 3))


